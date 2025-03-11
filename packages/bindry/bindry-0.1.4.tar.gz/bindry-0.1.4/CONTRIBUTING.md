## 🙌 Contributing Guide
We’re thrilled that you’re considering contributing to Bindry 🔗📚! Contributions from the community help make Bindry better, whether by reporting bugs, suggesting enhancements, improving documentation, or submitting code.

This guide will help you get started and understand our contribution process.

## 🛠️ How to Contribute
### 1. Reporting Issues

If you’ve encountered a bug, have a question, or want to suggest a feature:   
    1.1. **Check the issue** tracker to see if the issue already exists.   
    1.2. If it doesn’t, open a new issue.        
- Use a clear and descriptive title.        
- Provide as much context as possible (e.g., steps to reproduce, expected vs. actual behavior).

### 2. Suggesting Enhancements
Have an idea for a new feature or improvement? We’d love to hear it!
- Open a feature request and describe your suggestion in detail.

### 3. Contributing Code
**Steps to Submit Code Contributions:**

3.1. **Fork the repository**
- Click the "Fork" button on the top-right corner of the repository page.

3.2. **Clone your fork**
```bash
git clone https://github.com/hcleungca/bindry.git
cd bindry
```

3.3. **Set up the development environment**
- Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
- Run tests to ensure everything is working:
    ```bash
    pytest
    ```

3.4. **Create a new branch**

Use a descriptive branch name:
```bash
git checkout -b feature/my-new-feature
```

3.5. **Make your changes**
- Ensure your code adheres to the PEP 8 style guide.
- Add or update tests for your changes.

3.6. **Run tests**

Verify your changes don’t break existing functionality:
```bash
pytest
```

3.7. **Commit your changes**

Write clear and concise commit messages:
```bash
git add .
git commit -m "Add feature to support environment profiles"
```

3.8. Push to your fork
```bash
git push origin feature/my-new-feature
```

3.9. **Submit a pull request**
- Go to your fork on GitHub and click “New Pull Request.”
- Fill out the template, explaining what your changes do and why they’re needed.

## 🧪 Development Guidelines
- Testing:
    - Write unit tests for new features or bug fixes.
    - Ensure all tests pass before submitting your pull request.

- Code Style:
    - Follow Python’s PEP 8 style guide.
    - Use tools like black for code formatting and linting.

- Documentation:
    - Update the README or other docs for any new features or changes.

## 💡 Tips for Success
- Be respectful and considerate in discussions.
- Small, focused changes are easier to review than large, sweeping ones.
- Engage with reviewers if they request changes or clarification.

## 📝 Code of Conduct
By participating in this project, you agree to abide by our Code of Conduct.

## 🙏 Acknowledgments
Thank you for taking the time to contribute! Every bit of help is appreciated, whether it’s fixing a typo or adding a new feature. Together, we can make Bindry 🔗📚 even better!

