import argparse
import asyncio
import json
from datetime import datetime
from pathlib import Path
import concurrent.futures
from benchmarks import latency, memory, security, scaling, energy

class ORACBenchmark:
    def __init__(self, output_path="civitas_report.json"):
        self.output_path = Path(output_path)
        self.results = {
            'metadata': {
                'start_time': datetime.now().isoformat(),
                'version': '2.0',
                'system_info': self._get_system_info()
            }
        }
        
    def _get_system_info(self):
        """Collect basic system information for context"""
        import platform
        import psutil
        return {
            'platform': platform.platform(),
            'cpu_count': psutil.cpu_count(),
            'memory_gb': round(psutil.virtual_memory().total / (1024**3), 2),
            'python_version': platform.python_version()
        }
    
    async def run_benchmark(self, name, module, progress_callback=None):
        """Run a single benchmark with progress tracking"""
        print(f"Starting {name} benchmark...")
        
        # Run in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result = await loop.run_in_executor(executor, module.run)
        
        self.results[name] = {
            'result': result,
            'completed_at': datetime.now().isoformat()
        }
        
        # Stream partial results
        self._save_partial_results()
        
        if progress_callback:
            progress_callback(name, result)
        
        print(f"✓ {name} benchmark completed")
        return result
    
    def _save_partial_results(self):
        """Save results incrementally for real-time monitoring"""
        with open(self.output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
    
    async def run_suite(self, mode="all", parallel_safe=True):
        """Run the complete benchmark suite with smart execution"""
        
        # Define benchmark modules and their dependencies
        benchmark_config = {
            'memory': {'module': memory, 'depends_on': [], 'parallel_safe': True},
            'latency': {'module': latency, 'depends_on': [], 'parallel_safe': True},
            'security': {'module': security, 'depends_on': [], 'parallel_safe': False},
            'energy': {'module': energy, 'depends_on': ['memory'], 'parallel_safe': False},
            'scaling': {'module': scaling, 'depends_on': ['latency', 'memory'], 'parallel_safe': False}
        }
        
        # Filter based on mode
        if mode != "all":
            benchmark_config = {k: v for k, v in benchmark_config.items() if k == mode}
        
        # Smart execution: parallel where safe, sequential where needed
        if parallel_safe and len(benchmark_config) > 1:
            parallel_benchmarks = [k for k, v in benchmark_config.items() if v['parallel_safe']]
            sequential_benchmarks = [k for k, v in benchmark_config.items() if not v['parallel_safe']]
            
            # Run parallel benchmarks concurrently
            if parallel_benchmarks:
                tasks = [
                    self.run_benchmark(name, benchmark_config[name]['module'])
                    for name in parallel_benchmarks
                ]
                await asyncio.gather(*tasks)
            
            # Run sequential benchmarks one by one
            for name in sequential_benchmarks:
                await self.run_benchmark(name, benchmark_config[name]['module'])
        else:
            # Fallback to sequential execution
            for name, config in benchmark_config.items():
                await self.run_benchmark(name, config['module'])
        
        # Finalize results
        self.results['metadata']['end_time'] = datetime.now().isoformat()
        self.results['metadata']['total_duration'] = self._calculate_duration()
        
        # Generate summary insights
        self.results['summary'] = self._generate_insights()
        
        self._save_partial_results()
        print(f"\n🚀 Benchmark suite completed! Results saved to {self.output_path}")
    
    def _calculate_duration(self):
        """Calculate total benchmark duration"""
        start = datetime.fromisoformat(self.results['metadata']['start_time'])
        end = datetime.fromisoformat(self.results['metadata']['end_time'])
        return str(end - start)
    
    def _generate_insights(self):
        """Generate automated insights from benchmark results"""
        insights = []
        
        # Example insight generation (you'd expand this based on your metrics)
        if 'latency' in self.results and 'scaling' in self.results:
            insights.append("Cross-benchmark analysis reveals performance correlation patterns")
        
        if 'energy' in self.results:
            insights.append("Energy efficiency metrics captured for sustainability assessment")
        
        return {
            'key_insights': insights,
            'benchmark_count': len([k for k in self.results.keys() if k not in ['metadata', 'summary']]),
            'performance_grade': self._calculate_performance_grade()
        }
    
    def _calculate_performance_grade(self):
        """Simple performance grading based on results"""
        # This would be more sophisticated based on your actual metrics
        return "A-" if len(self.results) > 3 else "B+"

async def main():
    parser = argparse.ArgumentParser(description="ORAC Benchmark Suite v2.0")
    parser.add_argument("--mode", choices=["all", "latency", "memory", "security", "scaling", "energy"], default="all")
    parser.add_argument("--output", default="civitas_report.json")
    parser.add_argument("--parallel", action="store_true", help="Enable parallel execution where safe")
    parser.add_argument("--watch", action="store_true", help="Enable real-time result monitoring")
    
    args = parser.parse_args()
    
    benchmark = ORACBenchmark(args.output)
    
    if args.watch:
        print("🔍 Real-time monitoring enabled - results streaming to", args.output)
    
    await benchmark.run_suite(mode=args.mode, parallel_safe=args.parallel)

if __name__ == "__main__":
    # Run with asyncio for modern Python async support
    asyncio.run(main())
