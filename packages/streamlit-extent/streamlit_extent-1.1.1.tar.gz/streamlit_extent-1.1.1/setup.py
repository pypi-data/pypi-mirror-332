from setuptools import setup, find_packages

setup(
    name="streamlit-extent",  # Название пакета <button class="citation-flag" data-index="4">
    version="1.1.1",          # Версия (начните с 0.1.0)
    author='Voronov Andrey',        # Автор <button class="citation-flag" data-index="4">
    author_email="Vorona@email.com",  # Контактная почта <button class="citation-flag" data-index="4">
    description="Расширение для Streamlit, добавляющее дополнительные компоненты и функции",  # Краткое описание
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Автоматическое определение пакетов
    install_requires=[         # Зависимости
        "streamlit>=1.22.0",   # Минимальная версия Streamlit <button class="citation-flag" data-index="1"><button class="citation-flag" data-index="9">
    ],
    classifiers=[              # Классификаторы PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",   # Требуемая версия Python
)

