<template>
    <div class="w-[25vw] border-2 flex-wrap">
        <div class="data flex flex-row gap-2 max-w-max flex-wrap">
            <div
                v-for="(info, index) in data"
                :class="applyClass(index)"
                class="px-4">
                {{ info }}
            </div>
        </div>

        <div class="drop">
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
        <div class="flex w-full items-center justify-center gap-20">
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
                    styles.push("border-green-500");
                } else {
                    styles.push("border-blue-500");
                }
                return styles;
            },
        },
    };
</script>
