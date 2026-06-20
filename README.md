# 🚀 RAG Document Assistant

Sistema de búsqueda semántica sobre documentos utilizando **OpenAI**, **Pinecone** y **Python**.

Este proyecto implementa una arquitectura **RAG (Retrieval-Augmented Generation)** que permite consultar documentos mediante lenguaje natural. El sistema procesa documentos, genera embeddings, almacena información en una base de datos vectorial y utiliza modelos de lenguaje para responder preguntas basadas en el contenido proporcionado.

---

## 🎯 Objetivo

Comprender e implementar los fundamentos de los sistemas modernos de recuperación de información utilizados en aplicaciones de Inteligencia Artificial.

Durante el desarrollo de este proyecto se exploran conceptos como:

- Vector Databases
- Embeddings
- Semantic Search
- Chunking
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)

---

## 🛠 Tecnologías

- Python
- OpenAI API
- Pinecone
- Streamlit

---

## ⚙️ Arquitectura

```text
Documento
    ↓
Chunking
    ↓
Embeddings
    ↓
Pinecone (Vector Database)
    ↓
Búsqueda Semántica
    ↓
Contexto Relevante
    ↓
OpenAI
    ↓
Respuesta al Usuario
```

---

## 🔍 ¿Cómo funciona?

### 1. Carga del documento

El usuario carga un documento que será utilizado como fuente de conocimiento.

### 2. División en fragmentos

El documento se divide en pequeños bloques de texto (chunks) para facilitar su procesamiento.

### 3. Generación de embeddings

Cada fragmento se transforma en una representación vectorial mediante modelos de embeddings.

### 4. Almacenamiento vectorial

Los embeddings se almacenan en Pinecone junto con la información asociada.

### 5. Consulta del usuario

Cuando el usuario realiza una pregunta, la consulta también se convierte en un embedding.

### 6. Recuperación de contexto

Pinecone identifica los fragmentos más similares utilizando búsqueda por similitud vectorial.

### 7. Generación de respuesta

Los fragmentos recuperados se envían junto con la consulta al modelo de OpenAI, que genera una respuesta basada en el contexto encontrado.

---

## 📚 Conceptos Aprendidos

- Procesamiento de documentos
- Generación de embeddings
- Bases de datos vectoriales
- Búsqueda semántica
- Recuperación de contexto
- Arquitecturas RAG
- Integración con APIs de IA Generativa

---

## 🚀 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/rag-document-assistant.git
cd rag-document-assistant
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Configurar las credenciales necesarias:

```env
OPENAI_API_KEY=your_api_key
PINECONE_API_KEY=your_api_key
```

Ejecutar la aplicación:

```bash
streamlit run app.py
```

---

## 💡 Casos de Uso

- Asistentes documentales
- Bases de conocimiento empresariales
- Consulta de manuales técnicos
- Soporte interno
- Sistemas de preguntas y respuestas sobre documentación privada

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de aprendizaje en Ingeniería de IA, explorando técnicas modernas de búsqueda semántica y sistemas RAG utilizando OpenAI y Pinecone.
