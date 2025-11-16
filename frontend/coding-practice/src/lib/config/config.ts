// For static builds, VITE_BACKEND_URL must be set at build time
// For development, create a .env file with VITE_BACKEND_URL=http://localhost:5000
export const API_URL = import.meta.env.VITE_BACKEND_URL || '';