## 🛠 Python AI 协作风格指南 (v1.0)

### 1. 类型提示 (Type Hinting) —— **强制要求**
所有生成的代码必须符合 **PEP 484** 规范，严禁出现缺失类型的函数定义。
* **基础类型：** 必须标注所有函数参数及返回值。
* **复杂类型：** 优先使用内置集合类型（Python 3.9+），如 `list[str]` 而非 `List[str]`。
* **可选值：** 必须使用 `Optional[T]` 或 `T | None` 明确表示。
* **示例：**
    ```python
    def fetch_user_data(user_id: int, timeout: float = 5.0) -> dict[str, Any] | None:
        ...
    ```

### 2. 异步编程与框架规范
针对后端服务，默认采用异步优先原则：
* **框架偏好：** 优先使用 **FastAPI** 风格的路径定义。
* **I/O 操作：** 涉及数据库、网络请求或文件读写时，必须使用 `async` / `await`。
* **依赖注入：** 推荐使用框架原生的依赖注入模式（如 FastAPI 的 `Depends`）。

### 3. 文档与注释 (Documentation)
* **Docstrings：** 采用 **Google Style**。
* **内容要求：** 必须包含 `Args`、`Returns` 以及可能抛出的 `Raises` 异常说明。
* **示例：**
    ```python
    def calculate_metrics(data: list[float]) -> float:
        """计算数据集的加权平均值。

        Args:
            data: 输入的浮点数列表。

        Returns:
            计算得出的平均结果。
        """
    ```

### 4. 错误处理 (Error Handling)
* **禁止空异常捕获：** 严禁使用 `except: pass`。
* **精确性：** 必须捕获具体的异常类（如 `SQLAlchemyError`, `ValueError`）。
* **业务异常：** 推荐定义自定义异常类，并统一错误返回格式。

### 5. 命名与结构 (Naming & Structure)
* **变量/函数：** `snake_case` (蛇形命名法)。
* **类名：** `PascalCase` (大驼峰命名法)。
* **常量：** `UPPER_SNAKE_CASE` (大写蛇形命名法)。
* **工程结构：** 遵循模块化设计，逻辑层 (Service) 与 接入层 (Router) 必须解耦。

### 6. 现代工具集成
* **ORM：** 推荐使用 SQLAlchemy 2.0+ (Async) 或 Tortoise-ORM。
* **Pydantic：** 所有数据模型和配置验证必须使用 Pydantic V2。
* **Linting：** 代码需兼容 `ruff` 或 `flake8` 的静态检查要求。
