<script lang="ts">
    import CodeMirror from 'svelte-codemirror-editor';
    import { customTheme } from './customTheme';
    import { EditorView } from '@codemirror/view';
    import { java } from '@codemirror/lang-java';
    import { terminalSettings } from '$lib/config/terminalSettings.svelte';

    let {
        value = $bindable(),
        className = '',
        language: _language = undefined,
        editable = true
    } = $props();

    const styles = $derived({
        '.cm-content': {
            fontFamily: terminalSettings.fullFont,
            fontSize: `${terminalSettings.fontSize}px`,
            fontWeight: '500',
        },
        '&': {
            height: '100%',
            width: '100%',

        },
        '.cm-scroller': {
            overflow: 'auto'
        }
    });

    const extensions = $derived.by(() => {
        const currentExtensions = [customTheme, EditorView.lineWrapping];
        if (_language) {
            switch (_language) {
                case 'java':
                    currentExtensions.push(java());
                    break;
            }
        }
        return currentExtensions;
    });
</script>

<CodeMirror bind:value class={className} {extensions} {styles} {editable}/>