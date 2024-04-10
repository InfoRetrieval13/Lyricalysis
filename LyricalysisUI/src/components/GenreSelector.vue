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
            <select v-model="selectedGenre">
                <option
                    v-for="genre in genres"
                    :key="genre"
                    :value="genre">
                    {{ genre }}
                </option>
            </select>

            <select v-model="genreOperator">
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
        name: "GenreSelector",
        props: {
            data: Array,
        },
        data() {
            return {
                genres: ["Pop", "Rock", "Country", "Hip-Hop", "Rap", "Jazz", "Classical", "Electronic"],
                operators: ["AND", "OR"],
                selectedGenre: "",
                genreOperator: "",
            };
        },
        methods: {
            updateElement() {
                if (!this.selectedGenre || !this.genreOperator) {
                    return;
                }
                this.data.push(this.selectedGenre);
                this.data.push(this.genreOperator);
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
