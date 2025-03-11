import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // Proxy API requests to the backend during development
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  },
  // Configure build output
  build: {
    outDir: '../static/ui',
    emptyOutDir: true,
    sourcemap: true
  },
  // Resolve paths
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
})
