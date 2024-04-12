<template>
    <div class="w-[24vw] flex-wrap flex flex-col gap-2 items-center shadow-sm rounded-sm py-2">
        <div class="data flex flex-row gap-2 max-w-max flex-wrap items-start justify-start p-2">
            <div v-for="(info, index) in data">
                <div
                    v-if="index != 0"
                    :class="applyClass(index)">
                    {{ info }}
                </div>
            </div>
        </div>

        <div class="drop w-[10vw] flex items-start justify-between gap-2">
            <select v-model="genreOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
            <select v-model="selectedGenre">
                <option
                    value=""
                    disabled
                    selected>
                    Genres
                </option>
                <option
                    v-for="genre in genres"
                    :key="genre"
                    :value="genre">
                    {{ genre }}
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
        name: "GenreSelector",
        props: {
            data: Array,
        },
        data() {
            return {
                genres: [],
                operators: ["AND", "OR"],
                selectedGenre: "",
                genreOperator: "AND",
            };
        },
        async mounted() {
            await this.getGenres();
            console.log(this.genres);
        },
        methods: {
            async getGenres() {
                try {
                    let response = await fetch("https://lyricalysis-v6esf4zmfa-as.a.run.app/genres", {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                        },
                    });
                    let data = await response.json();
                    this.genres = data["genres"];
                    console.log(data["genres"]);
                } catch (error) {
                    console.error(error);
                }
            },
            updateElement() {
                if (!this.selectedGenre || !this.genreOperator) {
                    return;
                }
                this.data.push(this.genreOperator);
                this.data.push(this.selectedGenre);
            },
            removeElement() {
                this.data.pop();
                this.data.pop();
            },
            applyClass(index) {
                let styles = ["border-2", "px-4", "text-violet", "font-semibold", "font-inter"];
                if (index % 2 == 1) {
                    styles.push("border-greeny", "bg-green-100");
                } else {
                    styles.push("border-bluey", "bg-blue-100");
                }
                return styles;
            },
        },
    };
</script>
