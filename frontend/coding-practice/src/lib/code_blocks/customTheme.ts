import {createTheme} from 'thememirror';
import {tags as t} from '@lezer/highlight';

// TODO: highlighting makes it green fix dat
export const customTheme = createTheme({
	variant: 'dark',
	settings: {
		background: 'var(--surface)',
		foreground: 'var(--text-color)',
		caret: 'var(--highlight-high)',
		selection: 'color-mix(in srgb, var(--primary) 30%, transparent)', 
		lineHighlight: 'color-mix(in srgb, var(--overlay) 60%, transparent)',
		gutterBackground: 'transparent',
		gutterForeground: 'var(--muted)',
		
	},
	styles: [
		{
			tag: t.comment,
			color: 'var(--muted)',
		},
		{
			tag: t.variableName,
			color: 'var(--text-color)',
		},
		{
			tag: [t.string, t.special(t.brace)],
			color: 'var(--accent)',
		},
		{
			tag: t.number,
			color: 'var(--accent)',
		},
		{
			tag: t.bool,
			color: 'var(--accent)',
			fontWeight: 'bold'
		},
		{
			tag: t.null,
			color: 'var(--danger)',
			fontWeight: 'bold'
		},
		{
			tag: t.keyword,
			color: 'var(--secondary)',
		},
		{
			tag: t.operator,
			color: 'var(--secondary)',
		},
		{
			tag: t.className,
			color: 'var(--success)',
		},
		{
			tag: t.definition(t.className),
			color: 'var(--success)'
		},
		{
			tag: t.definition(t.typeName),
			color: 'var(--primary)',
		},
		{
			tag: t.typeName,
			color: 'var(--success)',
		},
		{
			tag: [t.function(t.variableName)],
			color: 'var(--primary)',
		},


		// these are used for html stuff
		{
			tag: t.angleBracket,
			color: 'var(--text-color)',
		},
		{
			tag: t.tagName,
			color: 'var(--text-color)',
		},
		{
			tag: t.attributeName,
			color: 'var(--text-color)',
		},
	],
});