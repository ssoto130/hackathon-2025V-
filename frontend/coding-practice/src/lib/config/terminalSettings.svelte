<script lang="ts" module>
    const defaultFont = 'monospace';
    const defaultFontSize = 16;
    const settingsKey = 'terminalSettings';

    export const terminalSettings = $state({
        font: defaultFont,
        fullFont: defaultFont,
        fontSize: defaultFontSize
    });

    export function updateFont(newFont?: string, fontSize?: number) {
        if (typeof newFont === 'string' && newFont.trim() !== ''){
            terminalSettings.font = newFont;
            terminalSettings.fullFont = `${newFont}, ${defaultFont}`;
            
            if (newFont !== defaultFont) {
                loadFont(newFont);
            }
        }
        if (typeof fontSize === 'number' && fontSize > 4) {
            terminalSettings.fontSize = fontSize;
        }
    }

    export function loadFont(fontName: string) {
        if (typeof document === 'undefined' || !fontName || fontName.trim() === '') return; // 💡 Guard against empty/invalid fontName

        const urlSafeFontName = fontName.replace(/\s/g, '+');
        const googleFontUrl = `https://fonts.googleapis.com/css2?family=${urlSafeFontName}:wght@400;700&display=swap`;
        
        const linkId = `gf-${urlSafeFontName.toLowerCase()}`;
        
        if (document.getElementById(linkId)) {
            console.log(`Font '${fontName}' already loaded.`);
            return;
        }

        const link = document.createElement('link');
        link.id = linkId;
        link.rel = 'stylesheet';
        link.href = googleFontUrl;
        
        link.onerror = () => {
             console.error(`Failed to load font: ${fontName}`);
             document.head.removeChild(link);
        };
        
        document.head.appendChild(link);
        console.log(`Loading font: ${fontName}`);
    }
    
    export function saveSettingsToCookies() {
        if (typeof document === 'undefined') return;

        try {
            const payload = {
                font: terminalSettings.font,
                fullFont: terminalSettings.fullFont,
                fontSize: terminalSettings.fontSize
            };

            const json = JSON.stringify(payload);
            localStorage.setItem(settingsKey, json);
        } catch (err) {
            console.error('saveSettingsToCookies failed:', err);
        }
    }

    export function getSettingsFromCookies() {
        if (typeof document === 'undefined') return; 

        try {
            const settingsValue = localStorage.getItem(settingsKey);
            if (!settingsValue) return;
            const settingsJson = JSON.parse(settingsValue);

            if (settingsJson.font) {
                updateFont(settingsJson.font);
            }
            if (typeof settingsJson.fontSize === 'number') {
                updateFont(undefined, settingsJson.fontSize);
            }
            
        } catch (err) {
            console.error('getSettingsFromCookies failed:', err);
        }
    }

    try {
        if (typeof document !== 'undefined') {
            getSettingsFromCookies();
        }
    } catch (e) {
        console.error('Early settings init failed:', e);
    }
</script>