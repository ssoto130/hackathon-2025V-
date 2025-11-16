import { browser } from "$app/environment";

export const themes = ['system', 'light', 'dark', 'rose-pine', 'rose-pine-light', 'dracula', 'monokai', 'nord'] as const;

export type Theme = (typeof themes)[number];

export function applyTheme(theme: Theme) {
    let themeToApply: string = 'dark'; 
    if (theme === 'system') {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        themeToApply = prefersDark ? 'dark' : 'light';
    } else {
        themeToApply = theme;
    }
    document.documentElement.setAttribute('data-theme', themeToApply.toLocaleLowerCase());
    localStorage.setItem('data-theme', themeToApply);
}

export function getCurrTheme(): Theme {
    if (!browser) {
        return 'system';
    }
    const storedTheme: string | null = localStorage.getItem('data-theme');
    if (storedTheme && themes.includes(storedTheme as Theme)) {
        return storedTheme as Theme;
    }
    return 'system';
}