<template>
    <div class="main w-screen h-screen flex flex-col items-center gap-10">
        <h1 class="text-9xl">Lyricalysis</h1>
        <div class="search-bar w-[80vw] min-h-[10vh] border-2 flex gap-10 flex-wrap">
            <div v-for="query in search">
                <div
                    v-if="query.type == 'artists'"
                    class="flex flex-row items-center">
                    <div class="type">
                        {{ query.type }}
                    </div>
                    <div class="start">
                        <select v-model="query.start">
                            <option value="HAS">HAS</option>
                            <option value="NOT">NOT</option>
                        </select>
                    </div>
                    <ArtistSelector :data="query.data" />
                    <div class="end">
                        <select v-model="query.end">
                            <option value="AND">AND</option>
                            <option value="OR">OR</option>
                        </select>
                    </div>
                </div>

                <div
                    v-else-if="query.type == 'genres'"
                    class="flex flex-row items-center">
                    <div class="type">
                        {{ query.type }}
                    </div>
                    <div class="start">
                        <select v-model="query.start">
                            <option value="HAS">HAS</option>
                            <option value="NOT">NOT</option>
                        </select>
                    </div>
                    <GenreSelector :data="query.data" />
                    <div class="end">
                        <select v-model="query.end">
                            <option value="AND">AND</option>
                            <option value="OR">OR</option>
                        </select>
                    </div>
                </div>

                <div
                    v-else-if="query.type == 'emotions'"
                    class="flex flex-row items-center">
                    <div class="type">
                        {{ query.type }}
                    </div>
                    <div class="start">
                        <select v-model="query.start">
                            <option value="HAS">HAS</option>
                            <option value="NOT">NOT</option>
                        </select>
                    </div>
                    <EmotionSelector :data="query.data" />
                    <div class="end">
                        <select v-model="query.end">
                            <option value="AND">AND</option>
                            <option value="OR">OR</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="controls">
            <div @click="addArtists">ARTISTS</div>

            <div @click="addGenres">GENRE</div>

            <div @click="addEmotions">EMOTION</div>
        </div>

        <div class="log">
            <button @click="logSearch">Search</button>
        </div>
    </div>
</template>

<script>
    import ArtistSelector from "./components/ArtistSelector.vue";
    import GenreSelector from "./components/GenreSelector.vue";
    import EmotionSelector from "./components/EmotionSelector.vue";
    export default {
        name: "App",
        data() {
            return {
                search: [],
            };
        },
        components: {
            ArtistSelector,
            GenreSelector,
            EmotionSelector,
        },
        methods: {
            addArtists() {
                this.search.push({ type: "artists", start: "HAS", data: [], end: "AND" });
            },
            addGenres() {
                this.search.push({ type: "genres", start: "HAS", data: [], end: "AND" });
            },
            addEmotions() {
                this.search.push({ type: "emotions", start: "HAS", data: [], end: "AND" });
            },
            logSearch() {
                console.log(this.search);
            },
        },
    };
</script>

<style>
    button {
        @apply w-40 h-10 bg-blue-500 text-white rounded-xl;
    }

    select {
        @apply min-w-10 h-10 bg-green-500 text-white px-3;
    }
</style>
