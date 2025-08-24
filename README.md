# ORAC Benchmark Suite

A comprehensive, next-generation benchmarking framework for system performance evaluation with real-time monitoring and intelligent test orchestration.

## 🚀 Features

- **Multi-domain Testing**: Comprehensive benchmarks across latency, memory, security, scaling, and energy efficiency
- **Smart Execution**: Parallel processing where safe, with dependency-aware scheduling  
- **Real-time Streaming**: Live results with immediate feedback for long-running tests
- **Automated Insights**: AI-powered analysis and performance grading
- **Modern Architecture**: Async-first design with Python 3.8+ support
- **Visualization Ready**: Direct integration with Grafana and dashboard tools

## 📊 Benchmark Categories

| Category | Description | Parallel Safe |
|----------|-------------|---------------|
| **Latency** | Network and I/O response time analysis | ✅ |
| **Memory** | RAM utilization and allocation patterns | ✅ |
| **Security** | Vulnerability scanning and hardening tests | ❌ |
| **Scaling** | Load handling and performance under stress | ❌ |
| **Energy** | Power consumption and efficiency metrics | ❌ |

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/orac-benchmark.git
cd orac-benchmark

# Install dependencies
pip install -r requirements.txt

# Optional: Install in development mode
pip install -e .
```

## ⚡ Quick Start

```bash
# Run all benchmarks
python orac_bench.py

# Run specific benchmark
python orac_bench.py --mode latency

# Enable parallel execution and real-time monitoring
python orac_bench.py --parallel --watch

# Custom output location
python orac_bench.py --output results/my_benchmark.json
```

## 🔧 Advanced Usage

### Parallel Execution
```bash
# Smart parallel execution (recommended)
python orac_bench.py --parallel --watch
```

### Integration with Monitoring
```bash
# Stream results for real-time dashboards
python orac_bench.py --watch --output /var/log/orac/results.json
```

### Programmatic Usage
```python
import asyncio
from orac_bench import ORACBenchmark

async def custom_benchmark():
    benchmark = ORACBenchmark("custom_results.json")
    await benchmark.run_suite(mode="latency", parallel_safe=True)
    return benchmark.results

# Run your custom benchmark
results = asyncio.run(custom_benchmark())
```

## 📈 Results Format

The benchmark outputs structured JSON with metadata, individual test results, and automated insights:

```json
{
  "metadata": {
    "start_time": "2025-08-24T10:30:00",
    "system_info": {
      "platform": "Linux-5.15.0",
      "cpu_count": 8,
      "memory_gb": 32.0
    }
  },
  "latency": {
    "result": {...},
    "completed_at": "2025-08-24T10:31:15"
  },
  "summary": {
    "performance_grade": "A-",
    "key_insights": [...]
  }
}
```

## 🎯 Roadmap

- [ ] **GPU Benchmarks**: CUDA and OpenCL performance testing
- [ ] **Container Support**: Docker and Kubernetes integration
- [ ] **Cloud Integration**: AWS/GCP/Azure native benchmarks
- [ ] **ML Workloads**: TensorFlow and PyTorch performance tests
- [ ] **Web Dashboard**: Built-in visualization interface

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements

- Python 3.8+
- psutil>=5.8.0
- asyncio (built-in)
- Additional benchmark-specific dependencies (see requirements.txt)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for the ORAC (Optimized Resource Allocation & Computation) project
- Inspired by modern cloud-native performance testing needs
- Community-driven benchmark definitions and thresholds

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/orac-benchmark/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/orac-benchmark/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/orac-benchmark/wiki)
