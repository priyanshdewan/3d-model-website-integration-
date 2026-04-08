# 🎨 Hunyuan3D React Frontend

A modern, responsive React interface for generating and viewing 3D models using the Hunyuan3D-2 backend. This frontend allows users to upload images and transform them into high-fidelity 3D assets in seconds.

## ✨ Features

- **Intuitive UI**: Simple drag-and-drop or click-to-upload interface.
- **Real-time Generation**: Communicates with the Hunyuan3D-2 FastAPI backend.
- **Interactive 3D Viewer**: Uses Google's `<model-viewer>` to display generated `.glb` models with support for:
  - Auto-rotation
  - Camera controls
  - Shadow intensity & realistic lighting
- **State Management**: Handles loading states, errors, and previewing images before generation.

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v16 or higher)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)
- A running Hunyuan3D-2 API server (see the root `README.md`)

### Installation

1. Navigate to the demo directory:
   ```bash
   cd react-3d-demo
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

### Development

Run the development server:
```bash
npm run dev
```
The app will typically be available at `http://localhost:5173`.

### Backend Configuration

By default, the application expects the API server to be running at `http://localhost:8081`. You can modify this in `src/ModelGenerator.jsx` if your server is running on a different port.

```javascript
const response = await fetch('http://localhost:8081/generate', { ... });
```

## 🛠️ Built With

- **React SDK**: Built with Vite for ultra-fast HMR.
- **Model-Viewer**: Web component for rendering 3D models.
- **Vanilla CSS**: Custom styling for a premium, modern feel.

## 📂 Project Structure

- `src/ModelGenerator.jsx`: Core component for image upload and API interaction.
- `src/ModelGenerator.css`: Custom styles for the generator interface.
- `public/`: Static assets and the `<model-viewer>` script inclusion.
