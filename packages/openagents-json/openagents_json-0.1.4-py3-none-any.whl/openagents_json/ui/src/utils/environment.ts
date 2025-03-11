/**
 * Environment utilities for accessing environment-specific configuration.
 */

/**
 * API base URL from environment variable with fallback to '/api'
 */
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

/**
 * Check if the application is running in development mode
 */
export const isDevelopment = import.meta.env.DEV;

/**
 * Check if the application is running in production mode
 */
export const isProduction = import.meta.env.PROD; 