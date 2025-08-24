# Contributing to ORAC Benchmark Suite

We love contributions! Whether you're fixing bugs, adding features, or improving documentation, your help makes ORAC better for everyone.

## 🚀 Quick Start for Contributors

1. **Fork & Clone**
   ```bash
   git clone https://github.com/yourusername/orac-benchmark.git
   cd orac-benchmark
   ```

2. **Set up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Run Tests**
   ```bash
   pytest tests/ -v
   ```

## 🛠️ Development Workflow

### Setting Up Your Environment

```bash
# Install with all development dependencies
pip install -e ".[dev,cloud,visualization]"

# Install pre-commit hooks (recommended)
pre-commit install
```

### Code Standards

We maintain high code quality standards:

- **Python 3.8+** compatibility required
- **Black** for code formatting: `black .`
- **Flake8** for linting: `flake8 .`
- **MyPy** for type checking: `mypy orac_bench.py`
- **Pytest** for testing with >90% coverage

### Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-amazing-feature
   ```

2. **Write Tests First** (TDD approach encouraged)
   ```bash
   # Add tests in tests/test_your_feature.py
   pytest tests/test_your_feature.py -v
   ```

3. **Implement Your Feature**
   - Follow existing code patterns
   - Add docstrings for public functions
   - Include type hints where applicable

4. **Test Everything**
   ```bash
   # Run full test suite
   pytest

   # Check code formatting
   black --check .
   
   # Lint code
   flake8 .
   
   # Type checking
   mypy orac_bench.py
   ```

## 📋 Types of Contributions

### 🐛 Bug Reports
Use the bug report template and include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version)
- Benchmark output/logs if applicable

### ✨ Feature Requests
- Describe the use case clearly
- Explain why this would benefit other users
- Consider implementation complexity
- Check if similar functionality exists

### 🚀 Code Contributions

#### Adding New Benchmarks
```python
# benchmarks/your_new_benchmark.py
def run():
    """
    Your benchmark implementation.
    
    Returns:
        dict: Results in standard ORAC format
    """
    return {
        'metric_name': value,
        'details': {...},
        'metadata': {...}
    }
```

#### Extending Core Framework
- Follow the async/await pattern
- Maintain backward compatibility
- Add comprehensive error handling
- Document breaking changes

### 📚 Documentation
- Fix typos, improve clarity
- Add examples and use cases  
- Update docstrings
- Contribute to the Wiki

## 🧪 Testing Guidelines

### Writing Tests
```python
# tests/test_new_feature.py
import pytest
from orac_bench import ORACBenchmark

@pytest.mark.asyncio
async def test_your_feature():
    benchmark = ORACBenchmark()
    result = await benchmark.run_benchmark('test', mock_module)
    assert result['status'] == 'completed'
```

### Test Categories
- **Unit Tests**: Individual functions/methods
- **Integration Tests**: Module interactions
- **End-to-End Tests**: Full benchmark runs
- **Performance Tests**: Regression detection

## 📊 Benchmark Standards

### Result Format
All benchmarks must return results in this format:
```python
{
    'primary_metric': float,  # Main performance indicator
    'secondary_metrics': {   # Additional measurements
        'throughput': float,
        'error_rate': float,
    },
    'metadata': {           # Test conditions
        'duration': float,
        'iterations': int,
        'timestamp': str,
    }
}
```

### Performance Considerations
- Minimize overhead in measurement code
- Use appropriate statistical methods
- Handle edge cases gracefully
- Provide meaningful error messages

## 🔍 Code Review Process

1. **Automated Checks**: All CI tests must pass
2. **Peer Review**: At least one maintainer approval required
3. **Performance Impact**: Benchmark any performance-affecting changes
4. **Documentation**: Update relevant docs with your changes

## 🎯 Priority Areas

We're particularly interested in contributions for:

- **New Benchmark Categories**: GPU, network, database, ML workloads
- **Cloud Integrations**: AWS, GCP, Azure native benchmarks  
- **Visualization**: Dashboard improvements, new chart types
- **Performance**: Optimization and scalability improvements
- **Platform Support**: Windows, macOS compatibility

## 🤝 Community Guidelines

- Be respectful and constructive in discussions
- Help newcomers get started
- Share knowledge through clear documentation
- Celebrate others' contributions

## 📞 Getting Help

- **Questions**: Use [GitHub Discussions](https://github.com/yourusername/orac-benchmark/discussions)
- **Chat**: Join our community Slack (link in README)
- **Issues**: Search existing issues before creating new ones

## 🏆 Recognition

Contributors are recognized in:
- CHANGELOG.md for each release
- GitHub contributors page
- Special thanks in documentation

## 📄 Legal Stuff

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project. We may ask you to sign a Contributor License Agreement (CLA) for larger contributions.

---

Thank you for making ORAC Benchmark Suite better! 🚀
