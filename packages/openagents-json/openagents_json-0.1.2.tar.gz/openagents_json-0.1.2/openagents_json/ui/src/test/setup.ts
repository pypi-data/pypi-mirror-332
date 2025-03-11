import { expect, afterEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';
import * as matchers from '@testing-library/jest-dom/matchers';

// Extend Vitest's expect with Testing Library matchers
expect.extend(matchers);

// Add TypeScript definitions for the matchers
declare module 'vitest' {
  interface Assertion<T> {
    toBeInTheDocument(): Assertion<T>;
    toBeVisible(): Assertion<T>;
    toHaveTextContent(text: string): Assertion<T>;
    toHaveAttribute(attr: string, value?: string): Assertion<T>;
  }
}

// Clean up after each test
afterEach(() => {
  cleanup();
  vi.resetAllMocks();
}); 