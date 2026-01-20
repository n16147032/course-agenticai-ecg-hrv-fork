import argparse
from hrv_agent.agent import HRVCoachAgent
from hrv_agent.config import Config

def main():
    parser = argparse.ArgumentParser(description="HRV Coach Pro v2.1")
    parser.add_argument('--record', type=str, required=True, help="Record ID (e.g. 100)")
    parser.add_argument('--dataset', type=str, default='mitdb', help="PhysioNet dataset")
    parser.add_argument('--out', type=str, default='outputs', help="Output directory")
    parser.add_argument('--use-openrouter', action='store_true', help="Use OpenRouter AI (Hardcoded: deepseek/deepseek-v3.2)")
    parser.add_argument('--channel', type=str, default='ECG', choices=['ECG', 'PPG'], help="Signal channel for local CSV data")
    
    args = parser.parse_args()
    
    # Choose agent type
    if args.use_openrouter:
        if not Config.is_openrouter_available():
            print("Error: OPENROUTER_API_KEY not found!")
            print("Please set it in .env file or use rule-based mode (remove --use-openrouter)")
            return
        
        print("Using OpenRouter-powered agent...")
        from hrv_agent.openrouter_agent import OpenRouterHRVAgent
        agent = OpenRouterHRVAgent(output_dir=args.out)
    else:
        print("Using rule-based agent...")
        agent = HRVCoachAgent(output_dir=args.out)
    
    # Pass channel for local data
    run_kwargs = {'channel': args.channel} if args.dataset == 'local_646' else {}
    agent.run(args.record, args.dataset, **run_kwargs)
    print(f"Done! Check {args.out} for results.")

if __name__ == "__main__":
    main()
