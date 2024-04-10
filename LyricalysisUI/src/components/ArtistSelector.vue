<template>
    <div class="w-[24vw] flex-wrap flex flex-col gap-2 items-center shadow-sm rounded-sm py-2">
        <div class="data flex flex-row gap-2 max-w-max flex-wrap items-start justify-start p-2">
            <div
                v-for="(info, index) in data"
                :class="applyClass(index)"
                class="px-4">
                {{ info }}
            </div>
        </div>

        <div class="drop w-[10vw] flex items-start justify-between gap-2">
            <select v-model="selectedArtist">
                <option
                    v-for="artist in artists"
                    :key="artist"
                    :value="artist">
                    {{ artist }}
                </option>
            </select>

            <select v-model="artistOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
        </div>
        <div class="flex w-[10vw] items-start justify-between gap-2">
            <button @click="updateElement">Add</button>
            <button @click="removeElement">Clear Latest</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ArtistSelector",
        props: {
            data: Array,
        },
        data() {
            return {
                artists: ["Taylor Swift", "Saylor Twift", "League of Legends", "DOTA"],
                operators: ["AND", "OR"],
                selectedArtist: "",
                artistOperator: "",
            };
        },
        methods: {
            updateElement() {
                if (!this.selectedArtist || !this.artistOperator) {
                    return;
                }
                this.data.push(this.selectedArtist);
                this.data.push(this.artistOperator);
            },
            removeElement() {
                this.data.pop();
                this.data.pop();
            },
            applyClass(index) {
                let styles = ["border-2"];
                if (index % 2 == 0) {
                    styles.push("border-green-500", "bg-green-100");
                } else {
                    styles.push("border-blue-500", "bg-blue-100");
                }
                return styles;
            },
        },
    };
</script>
