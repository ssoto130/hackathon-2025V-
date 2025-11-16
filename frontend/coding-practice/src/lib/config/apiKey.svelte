<script lang="ts" module>
    export const apiKey = $state({key: ''});

    export function updateKey(newKey: string, saveToCookies: boolean = false) {
        apiKey.key = newKey;
        if (saveToCookies){
            localStorage.setItem('gemKey', JSON.stringify(apiKey.key));
        } else {
            localStorage.removeItem('gemKey');
        }
    }

    export function loadKey() {
        const savedKey: string | null = localStorage.getItem('gemKey');
        if (savedKey) {
            apiKey.key = JSON.parse(savedKey);
        }
    }
</script>
