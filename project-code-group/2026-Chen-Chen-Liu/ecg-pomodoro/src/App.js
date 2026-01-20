import React, { useEffect, useMemo, useReducer, useRef, useState } from "react";
import "./App.css";

const SETTINGS_KEY = "pomodoro_settings_v1";
const MIN_WORK_MINUTES = 15;
const MIN_REST_MINUTES = 1;

const ECG_API = "http://127.0.0.1:8001";
const AI_API = "http://127.0.0.1:8002";

// Demo: work 模式下每隔幾秒「收集一段 segment」(實際專案可改成接藍牙/串流再切段)
const SEGMENT_EVERY_MS = 10_000;

function clampInt(value, min, max) {
    if (!Number.isFinite(value)) return min;
    return Math.max(min, Math.min(max, Math.trunc(value)));
}

function loadSettings() {
    try {
        const raw = localStorage.getItem(SETTINGS_KEY);
        if (!raw) return { workMinutes: 25, restMinutes: 5 };
        const p = JSON.parse(raw);
        return {
            workMinutes: clampInt(p.workMinutes, MIN_WORK_MINUTES, 180),
            restMinutes: clampInt(p.restMinutes, MIN_REST_MINUTES, 60),
        };
    } catch {
        return { workMinutes: 25, restMinutes: 5 };
    }
}

function saveSettings(settings) {
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
}

function formatMMSS(ms) {
    const totalSec = Math.ceil(Math.max(0, ms) / 1000);
    const mm = Math.floor(totalSec / 60);
    const ss = totalSec % 60;
    return `${String(mm).padStart(2, "0")}:${String(ss).padStart(2, "0")}`;
}

function remainingMs(endsAtMs, nowMs) {
    return Math.max(0, endsAtMs - nowMs);
}

function makeWorkEndsAt(settings, nowMs) {
    return nowMs + settings.workMinutes * 60_000;
}

function makeRestEndsAt(settings, nowMs) {
    return nowMs + settings.restMinutes * 60_000;
}

// ---------- Pomodoro state machine ----------
function initState() {
    return {
        kind: "HOME", // HOME | CONFIG | WORK | PAUSE | REST
        settings: loadSettings(),
        draft: null,
        endsAtMs: null,
        remainingMs: null,
    };
}

function reducer(state, action) {
    switch (action.type) {
        case "GO_HOME":
            return {
                ...state,
                kind: "HOME",
                draft: null,
                endsAtMs: null,
                remainingMs: null,
            };
        case "GO_CONFIG":
            return { ...state, kind: "CONFIG", draft: { ...state.settings } };
        case "SET_WORK_MINUTES":
            if (state.kind !== "CONFIG") return state;
            return {
                ...state,
                draft: {
                    ...state.draft,
                    workMinutes: clampInt(action.value, MIN_WORK_MINUTES, 180),
                },
            };
        case "SET_REST_MINUTES":
            if (state.kind !== "CONFIG") return state;
            return {
                ...state,
                draft: {
                    ...state.draft,
                    restMinutes: clampInt(action.value, MIN_REST_MINUTES, 60),
                },
            };
        case "SAVE_CONFIG":
            if (state.kind !== "CONFIG") return state;
            return {
                ...state,
                kind: "HOME",
                settings: state.draft,
                draft: null,
            };

        case "START_WORK":
            if (state.kind !== "HOME" && state.kind !== "REST") return state;
            return {
                ...state,
                kind: "WORK",
                endsAtMs: makeWorkEndsAt(state.settings, action.nowMs),
                remainingMs: null,
            };

        case "PAUSE":
            if (state.kind !== "WORK") return state;
            return {
                ...state,
                kind: "PAUSE",
                remainingMs: remainingMs(state.endsAtMs, action.nowMs),
                endsAtMs: null,
            };

        case "RESUME":
            if (state.kind !== "PAUSE") return state;
            return {
                ...state,
                kind: "WORK",
                endsAtMs: action.nowMs + state.remainingMs,
                remainingMs: null,
            };

        case "FORCE_REST":
            if (state.kind !== "WORK") return state;
            return {
                ...state,
                kind: "REST",
                endsAtMs: makeRestEndsAt(state.settings, action.nowMs),
                remainingMs: null,
            };

        case "SKIP_REST":
            if (state.kind !== "REST") return state;
            return {
                ...state,
                kind: "WORK",
                endsAtMs: makeWorkEndsAt(state.settings, action.nowMs),
                remainingMs: null,
            };

        case "TICK":
            if (state.kind === "WORK" && action.nowMs >= state.endsAtMs) {
                return {
                    ...state,
                    kind: "REST",
                    endsAtMs: makeRestEndsAt(state.settings, action.nowMs),
                };
            }
            if (state.kind === "REST" && action.nowMs >= state.endsAtMs) {
                return {
                    ...state,
                    kind: "HOME",
                    endsAtMs: null,
                    remainingMs: null,
                };
            }
            return state;

        default:
            return state;
    }
}

// ---------- HTTP helper ----------
async function postJson(url, body) {
    const r = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
    });
    if (!r.ok) throw new Error(`HTTP ${r.status} at ${url}`);
    return await r.json();
}

// ---------- Demo ECG segment generator (same as your original demo) ----------
function makeDemoEcgSegment({
    nowMs,
    segmentId,
    samplingRateHz = 360,
    seconds = 30,
    mode = "stress", // "stress" | "relax"
}) {
    const sr = samplingRateHz;
    const n = sr * seconds;

    // 目標心率
    const targetHr = mode === "stress" ? 95 : 65;
    const baseRR = 60 / targetHr; // sec per beat

    // RR 抖動：relax 比 stress 大
    const jitterSec = mode === "stress" ? 0.03 : 0.09; // ~30ms vs 90ms

    // 產生 R-peak 時間點序列（秒）
    const peakTimes = [];
    let t = 0.4; // 避免太靠近 0
    while (t < seconds - 0.2) {
        const j = (Math.random() * 2 - 1) * jitterSec;
        t += Math.max(0.35, baseRR + j); // 下限避免過快
        if (t < seconds) peakTimes.push(t);
    }

    // 合成訊號：底噪 + R spike + 簡單呼吸/漂移
    const samples = Array.from({ length: n }, (_, i) => {
        const ts = i / sr;

        // baseline wander (0.25 Hz) + 小噪聲
        const wander = Math.sin(2 * Math.PI * 0.25 * ts) * 150;
        const noise = (Math.random() * 2 - 1) * 60;

        // R-peak spike：用窄高斯脈衝
        let spike = 0;
        for (const pt of peakTimes) {
            const dt = ts - pt;
            spike += 6500 * Math.exp(-(dt * dt) / (2 * 0.003 * 0.003)); // sigma=3ms
        }

        const v = 30000 + wander + noise + spike;
        return [Math.round(v)];
    });

    return {
        schema_version: "ecg-seg/v1",
        segment_id: segmentId || `seg_${nowMs}`,
        sampling_rate_hz: sr,
        start_time_unix_ms: nowMs,
        channels: [{ name: "ECG", unit: "adc", lead: "CH1" }],
        samples,
    };
}

export default function App() {
    const [tab, setTab] = useState("pomodoro"); // pomodoro | demo
    const [state, dispatch] = useReducer(reducer, undefined, initState);
    const [nowMs, setNowMs] = useState(() => Date.now());

    // Work session buffers
    const [sessionId, setSessionId] = useState("");
    const [workStartMs, setWorkStartMs] = useState(null);
    const [workSegments, setWorkSegments] = useState([]);

    // Outputs (for UI)
    const [pomodoroSummary, setPomodoroSummary] = useState(null);
    const [aiAdvice, setAiAdvice] = useState(null);

    // Demo tab outputs
    const [demoStatus, setDemoStatus] = useState("");
    const [errorMsg, setErrorMsg] = useState("");

    // Prevent duplicate finalize
    const finalizedRef = useRef(false);

    // Global timer tick
    useEffect(() => {
        const id = window.setInterval(() => {
            const n = Date.now();
            setNowMs(n);
            dispatch({ type: "TICK", nowMs: n });
        }, 250);
        return () => window.clearInterval(id);
    }, []);

    // Persist settings
    useEffect(() => {
        if (state.kind === "HOME") saveSettings(state.settings);
    }, [state.kind, state.settings]);

    const msLeft = useMemo(() => {
        if (state.kind === "WORK" || state.kind === "REST")
            return remainingMs(state.endsAtMs, nowMs);
        if (state.kind === "PAUSE") return state.remainingMs;
        return 0;
    }, [state, nowMs]);

    // When entering WORK: reset buffers
    useEffect(() => {
        if (state.kind !== "WORK") return;

        const sid = `pomodoro_${Date.now()}`;
        setSessionId(sid);
        setWorkStartMs(Date.now());
        setWorkSegments([]);
        setPomodoroSummary(null);
        setAiAdvice(null);
        setErrorMsg("");
        finalizedRef.current = false;
    }, [state.kind]);

    // During WORK: collect segments periodically (demo)
    useEffect(() => {
        if (state.kind !== "WORK") return;

        const id = window.setInterval(() => {
            const t = Date.now();
            const seg = makeDemoEcgSegment({
                nowMs: t,
                segmentId: `work_${t}`,
                mode: "stress",
            });
            setWorkSegments((prev) => [...prev, seg]);
        }, SEGMENT_EVERY_MS);

        return () => window.clearInterval(id);
    }, [state.kind]);

    // Finalize work when entering REST (call ECG summary + AI advice once)
    useEffect(() => {
        if (state.kind !== "REST") return;
        if (finalizedRef.current) return;
        finalizedRef.current = true;

        (async () => {
            try {
                setErrorMsg("");

                const endMs = Date.now();
                const startMs = workStartMs ?? endMs;

                // If no segments collected (e.g., user instantly force rest), create 1 segment.
                const segs = workSegments.length
                    ? workSegments
                    : [
                          makeDemoEcgSegment({
                              nowMs: startMs,
                              segmentId: `work_${startMs}`,
                          }),
                      ];

                const req = {
                    schema_version: "pomodoro-work/v1",
                    user_id: "demo_user",
                    session_id: sessionId || `pomodoro_${startMs}`,
                    work_start_unix_ms: startMs,
                    work_end_unix_ms: endMs,
                    segments: segs,
                };

                const summary = await postJson(
                    `${ECG_API}/ecg/pomodoro/end`,
                    req
                );
                setPomodoroSummary(summary);

                const advice = await postJson(
                    `${AI_API}/ai/pomodoro/advice`,
                    summary
                );
                setAiAdvice(advice);
            } catch (e) {
                setErrorMsg(String(e.message || e));
            }
        })();
    }, [state.kind, workSegments, workStartMs, sessionId]);

    // ---------- Demo tab: run pipeline quickly ----------
    async function runDemo() {
        setErrorMsg("");
        setPomodoroSummary(null);
        setAiAdvice(null);
        setDemoStatus("Running…");

        try {
            const start = Date.now();
            const segments = Array.from({ length: 3 }, (_, k) => {
                const t = start + k * 60_000;
                const mode = k < 2 ? "stress" : "relax";
                return makeDemoEcgSegment({
                    nowMs: t,
                    segmentId: `demo_${t}`,
                    mode,
                });
            });

            const req = {
                schema_version: "pomodoro-work/v1",
                user_id: "demo_user",
                session_id: `demo_session_${start}`,
                work_start_unix_ms: start,
                work_end_unix_ms: start + 3 * 60_000,
                segments,
            };

            const summary = await postJson(`${ECG_API}/ecg/pomodoro/end`, req);
            setPomodoroSummary(summary);

            const advice = await postJson(
                `${AI_API}/ai/pomodoro/advice`,
                summary
            );
            setAiAdvice(advice);

            setDemoStatus("Done.");
        } catch (e) {
            setDemoStatus("");
            setErrorMsg(String(e.message || e));
        }
    }

    return (
        <div className="container">
            <h1>ECG Pomodoro MVP</h1>

            <div className="row">
                <button
                    onClick={() => setTab("pomodoro")}
                    className={`tab ${tab === "pomodoro" ? "primary" : ""}`}
                >
                    Pomodoro
                </button>
                <button
                    onClick={() => setTab("demo")}
                    className={`tab ${tab === "demo" ? "primary" : ""}`}
                >
                    Demo Pipeline
                </button>
            </div>

            {tab === "pomodoro" && (
                <>
                    <div className="badge">{state.kind}</div>

                    {state.kind === "HOME" && (
                        <>
                            <p className="hint">
                                Work: {state.settings.workMinutes} min / Rest:{" "}
                                {state.settings.restMinutes} min
                            </p>
                            <div className="row">
                                <button
                                    onClick={() =>
                                        dispatch({
                                            type: "START_WORK",
                                            nowMs: Date.now(),
                                        })
                                    }
                                >
                                    Start
                                </button>
                                <button
                                    onClick={() =>
                                        dispatch({ type: "GO_CONFIG" })
                                    }
                                >
                                    Settings
                                </button>
                            </div>
                        </>
                    )}

                    {state.kind === "CONFIG" && (
                        <>
                            <p className="hint">
                                工作最短 {MIN_WORK_MINUTES} 分鐘；休息最短{" "}
                                {MIN_REST_MINUTES} 分鐘。
                            </p>
                            <div className="form">
                                <label>
                                    Work minutes
                                    <input
                                        type="number"
                                        step="1"
                                        min={MIN_WORK_MINUTES}
                                        value={state.draft.workMinutes}
                                        onChange={(e) =>
                                            dispatch({
                                                type: "SET_WORK_MINUTES",
                                                value: Number(e.target.value),
                                            })
                                        }
                                    />
                                </label>
                                <label>
                                    Rest minutes
                                    <input
                                        type="number"
                                        step="1"
                                        min={MIN_REST_MINUTES}
                                        value={state.draft.restMinutes}
                                        onChange={(e) =>
                                            dispatch({
                                                type: "SET_REST_MINUTES",
                                                value: Number(e.target.value),
                                            })
                                        }
                                    />
                                </label>
                            </div>
                            <div className="row">
                                <button
                                    onClick={() =>
                                        dispatch({ type: "SAVE_CONFIG" })
                                    }
                                >
                                    Save
                                </button>
                                <button
                                    onClick={() =>
                                        dispatch({ type: "GO_HOME" })
                                    }
                                >
                                    Cancel
                                </button>
                            </div>
                        </>
                    )}

                    {(state.kind === "WORK" ||
                        state.kind === "PAUSE" ||
                        state.kind === "REST") && (
                        <>
                            <div className="time">{formatMMSS(msLeft)}</div>

                            {state.kind === "WORK" && (
                                <div className="row">
                                    <button
                                        onClick={() =>
                                            dispatch({
                                                type: "PAUSE",
                                                nowMs: Date.now(),
                                            })
                                        }
                                    >
                                        Pause
                                    </button>
                                    <button
                                        onClick={() =>
                                            dispatch({
                                                type: "FORCE_REST",
                                                nowMs: Date.now(),
                                            })
                                        }
                                    >
                                        Force Rest
                                    </button>
                                    <button
                                        onClick={() =>
                                            dispatch({ type: "GO_HOME" })
                                        }
                                    >
                                        Stop
                                    </button>
                                </div>
                            )}

                            {state.kind === "PAUSE" && (
                                <div className="row">
                                    <button
                                        onClick={() =>
                                            dispatch({
                                                type: "RESUME",
                                                nowMs: Date.now(),
                                            })
                                        }
                                    >
                                        Resume
                                    </button>
                                    <button
                                        onClick={() =>
                                            dispatch({ type: "GO_HOME" })
                                        }
                                    >
                                        Stop
                                    </button>
                                </div>
                            )}

                            {state.kind === "REST" && (
                                <>
                                    <p className="hint">
                                        休息中：已送出工作時段摘要給 AI 產生建議
                                    </p>
                                    <div className="row">
                                        <button
                                            onClick={() =>
                                                dispatch({
                                                    type: "SKIP_REST",
                                                    nowMs: Date.now(),
                                                })
                                            }
                                        >
                                            Skip Rest
                                        </button>
                                        <button
                                            onClick={() =>
                                                dispatch({ type: "GO_HOME" })
                                            }
                                        >
                                            Stop
                                        </button>
                                    </div>
                                </>
                            )}
                        </>
                    )}

                    {errorMsg && <pre className="error">{errorMsg}</pre>}

                    {pomodoroSummary && (
                        <>
                            <h3>Pomodoro Summary</h3>
                            <pre className="box">
                                {JSON.stringify(pomodoroSummary, null, 2)}
                            </pre>
                        </>
                    )}

                    {aiAdvice && (
                        <>
                            <h3>AI Advice</h3>
                            <div className="card">
                                <div className="cardTitle">
                                    {aiAdvice.title}
                                </div>
                                <ul>
                                    {(aiAdvice.bullets || []).map((b, i) => (
                                        <li key={i}>{b}</li>
                                    ))}
                                </ul>
                                <div className="cardHint">
                                    {aiAdvice.safety_note}
                                </div>
                            </div>
                            <pre className="box">
                                {JSON.stringify(aiAdvice, null, 2)}
                            </pre>
                        </>
                    )}
                </>
            )}

            {tab === "demo" && (
                <>
                    <p className="hint">
                        先啟動兩個 service：ECG(8001)、AI(8002)，再按 Run Demo
                        測試「summary → advice」介面。
                    </p>
                    <div className="row">
                        <button onClick={runDemo}>Run Demo</button>
                        <a
                            href={`${ECG_API}/docs`}
                            target="_blank"
                            rel="noreferrer"
                        >
                            ECG docs
                        </a>
                        <a
                            href={`${AI_API}/docs`}
                            target="_blank"
                            rel="noreferrer"
                        >
                            AI docs
                        </a>
                    </div>

                    {demoStatus && <div className="hint">{demoStatus}</div>}
                    {errorMsg && <pre className="error">{errorMsg}</pre>}

                    {pomodoroSummary && (
                        <>
                            <h3>Pomodoro Summary</h3>
                            <pre className="box">
                                {JSON.stringify(pomodoroSummary, null, 2)}
                            </pre>
                        </>
                    )}
                    {aiAdvice && (
                        <>
                            <h3>AI Advice</h3>
                            <pre className="box">
                                {JSON.stringify(aiAdvice, null, 2)}
                            </pre>
                        </>
                    )}
                </>
            )}
        </div>
    );
}
