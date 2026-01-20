import streamlit as st
import os
import glob
from hrv_agent.agent import HRVCoachAgent
from hrv_agent.config import Config
import pandas as pd
import json

st.set_page_config(page_title="HRV Coach Pro", page_icon="🫀", layout="wide")

# Professional CSS Styling
st.markdown("""
<style>
    /* Modern Typography & Colors */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, .main {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background-color: #0e1117;
    }
    
    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Headers Styling */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .stHeader {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff8a8a 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Container Spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Divider Polish */
    hr {
        margin: 2em 0;
        opacity: 0.1;
    }
    
    /* Tables/Dataframes */
    [data-testid="stDataFrame"] {
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
col_title, col_status = st.columns([3, 1])
with col_title:
    st.markdown('<h1 class="stHeader">HRV Coach Pro v2.1</h1>', unsafe_allow_html=True)
    st.markdown("##### Autonomous Agent System for Clinical HRV Intelligence")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    with st.expander("🤖 Agent Settings", expanded=True):
        agent_mode = st.radio(
            "Agent Mode",
            ["📊 Rule-Based", "🧠 OpenRouter AI"],
            help="Choose between rule-based or AI-powered analysis"
        )
        use_ai = "OpenRouter" in agent_mode
        
        if use_ai:
            openrouter_key = st.text_input(
                "OpenRouter API Key",
                type="password",
                placeholder="sk-or-...",
                value=Config.get_openrouter_key()
            )
            if openrouter_key: os.environ['OPENROUTER_API_KEY'] = openrouter_key
            
            st.info(f"🚀 Using DeepSeek V3.2 (`{Config.OPENROUTER_MODEL}`) via OpenRouter")

    with st.expander("📂 Data Source", expanded=True):
        data_source = st.selectbox(
            "Select Source",
            ["PhysioNet (WFDB)", "Local 646 Data (CSV)"]
        )

        if data_source == "PhysioNet (WFDB)":
            dataset = st.text_input("Dataset", "mitdb")
            record_id = st.text_input("Record ID", "100")
        else:
            dataset = "local_646"
            if os.path.exists("646_data"):
                csv_files = [f for f in os.listdir("646_data") if f.endswith(".csv")]
                if csv_files:
                    record_id = st.selectbox("Select CSV File", csv_files)
                else:
                    st.error("No CSV files found")
                    record_id = ""
            else:
                st.error("646_data/ not found")
                record_id = ""
        
        signal_channel = st.selectbox("Channel", ["ECG", "PPG"]) if dataset == "local_646" else "ECG"

    with st.expander("🛠️ Advanced"):
        output_dir = st.text_input("Output Dir", "outputs/run_gui")

    st.markdown("---")
    run_button = st.button("🚀 Run Analysis", type="primary", use_container_width=True)

# Main Interface
if run_button:
    if "AI" in agent_mode and not (os.getenv('GEMINI_API_KEY') or os.getenv('DEEPSEEK_API_KEY')):
        st.error("❌ Please provide an API key for the selected AI agent")
    elif not record_id:
        st.error("❌ Please select a record first")
    else:
        with st.spinner(f"Agent is analyzing {record_id}..."):
            try:
                if "OpenRouter" in agent_mode:
                    from hrv_agent.openrouter_agent import OpenRouterHRVAgent
                    agent = OpenRouterHRVAgent(output_dir=output_dir)
                else:
                    agent = HRVCoachAgent(output_dir=output_dir)
                
                run_kwargs = {'channel': signal_channel} if dataset == 'local_646' else {}
                result = agent.run(record_id, dataset, **run_kwargs)
                
                if result['grade'] == 'Reject':
                    st.error(f"Analysis Failed: {result['reason']}")
                else:
                    st.success("✅ Analysis Complete!")
                    st.balloons()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Results Display
if os.path.exists(output_dir):
    # Load Data
    gemini_log = os.path.join(output_dir, "gemini_log.json")
    regular_log = os.path.join(output_dir, "agent_log.json")
    plots_file = os.path.join(output_dir, "plots.png")
    gemini_report = os.path.join(output_dir, "gemini_report.md")
    regular_report = os.path.join(output_dir, "report.md")

    log_data = None
    if os.path.exists(gemini_log):
        with open(gemini_log, 'r') as f: log_data = json.load(f)
    elif os.path.exists(regular_log):
        with open(regular_log, 'r') as f: log_data = json.load(f)

    if log_data:
        # Top Row: Health Status & Critical Metrics
        grade = log_data.get('grade', 'N/A')
        grade_color = "#28a745" if grade == 'A' else "#ffc107" if grade == 'B' else "#dc3545"
        
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <h3 style="margin: 0; margin-right: 15px;">📊 Intelligence Overview</h3>
                <span style="background-color: {grade_color}; color: white; padding: 4px 12px; border-radius: 15px; font-weight: bold; font-size: 0.9em;">
                    SIGNAL QUALITY: GRADE {grade}
                </span>
            </div>
        """, unsafe_allow_html=True)
        
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        
        # Display key metrics with health interpretations
        hr = log_data.get('metrics', {}).get('mean_hr', 0)
        sdnn = log_data.get('metrics', {}).get('sdnn', 0)
        rmssd = log_data.get('metrics', {}).get('rmssd', 0)
        
        m_col1.metric("❤️ Mean Heart Rate", f"{hr:.1f} BPM")
        m_col2.metric("📉 SDNN (Total Power)", f"{sdnn:.1f} ms")
        m_col3.metric("📈 RMSSD (Vagal Tone)", f"{rmssd:.1f} ms")
        m_col4.metric("⚖️ Autonomic State", "Balanced" if sdnn > 50 else "Stressed")
        
        st.divider()

        # Split into two main columns
        left_col, right_col = st.columns([1, 1], gap="large")

        with left_col:
            # 1. Clinical Report Section
            st.subheader("📄 Clinical Summary")
            
            clinical_text = ""
            if os.path.exists(gemini_report):
                with open(gemini_report, 'r', encoding='utf-8') as f:
                    clinical_text = f.read()
                    st.markdown(clinical_text)
            elif os.path.exists(regular_report):
                with open(regular_report, 'r', encoding='utf-8') as f:
                    clinical_text = f.read()
                    st.markdown(clinical_text)
            
            # PDF Download Button
            if clinical_text and log_data:
                st.divider()
                if st.button("📥 Download Report as PDF", type="primary", use_container_width=True):
                    try:
                        from hrv_agent.pdf_generator import generate_pdf_report
                        
                        pdf_path = os.path.join(output_dir, "hrv_report.pdf")
                        generate_pdf_report(
                            output_path=pdf_path,
                            record_id=log_data.get('record_id', 'Unknown'),
                            dataset=log_data.get('dataset', 'Unknown'),
                            grade=log_data.get('grade', 'N/A'),
                            metrics=log_data.get('metrics', {}),
                            clinical_summary=clinical_text,
                            plot_path=plots_file if os.path.exists(plots_file) else None
                        )
                        
                        with open(pdf_path, 'rb') as pdf_file:
                            st.download_button(
                                label="💾 Click to Download PDF",
                                data=pdf_file,
                                file_name=f"HRV_Report_{log_data.get('record_id', 'report')}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        st.success("✅ PDF generated successfully!")
                    except Exception as e:
                        st.error(f"Error generating PDF: {str(e)}")
            
            st.divider()
            
            # 3. Detailed Metrics Section
            st.subheader("📊 Primary HRV Metrics")
            metrics = log_data.get('metrics', {})
            df_metrics = pd.DataFrame([metrics]).T.reset_index()
            df_metrics.columns = ['Metric', 'Value']
            
            # Styling the table
            def highlight_metrics(val):
                if isinstance(val, (int, float)):
                    if val > 100: return 'color: #ff4b4b; font-weight: bold'
                    if val < 40: return 'color: #ffc107; font-weight: bold'
                return ''

            st.dataframe(
                df_metrics.style.applymap(highlight_metrics, subset=['Value']),
                use_container_width=True, 
                hide_index=True
            )

        with right_col:
            # 2. Visualizations Section
            st.subheader("🖼️ Signal Visualization")
            
            if os.path.exists(plots_file):
                st.image(plots_file, use_container_width=True)
            else:
                st.info("No plot found.")
                
            st.divider()

            # 4. Agent Logic Section
            st.subheader("🤖 Agent Reasoning")
            st.write(f"**Strategy:** `{log_data.get('strategy')}` | **Detector:** `{log_data.get('detector')}`")
            with st.expander("View Processing History"):
                st.table(pd.DataFrame(log_data.get('history', [])))

else:
    st.info("👋 Welcome! Configure settings in the sidebar and click **Run Analysis** to start.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("HRV Coach Pro v2.1 | [Docs](./README.md)")
