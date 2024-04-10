<template>
    <div class="main w-screen h-screen flex flex-col items-center gap-10">
        <h1 class="text-9xl">Lyricalysis</h1>
        <div
            class="search-bar items-start justify-start w-[95vw] min-h-[10vh] border-b-4 flex flex-wrap"
            style="row-gap: 1rem">
            <div
                v-for="query in search"
                class="flex items-start w-[30vw]">
                <div
                    v-if="query.type == 'artists'"
                    class="flex flex-row items-center artists w-full">
                    <div class="front">
                        <div class="type">
                            {{ query.type }}
                        </div>
                        <div class="start">
                            <select v-model="query.start">
                                <option value="HAS">HAS</option>
                                <option value="NOT">NOT</option>
                            </select>
                        </div>
                    </div>
                    <ArtistSelector :data="query.data" />
                </div>

                <div
                    v-else-if="query.type == 'genres'"
                    class="flex flex-row items-center genres w-full">
                    <div class="front">
                        <div class="type">
                            {{ query.type }}
                        </div>
                        <div class="start">
                            <select v-model="query.start">
                                <option value="HAS">HAS</option>
                                <option value="NOT">NOT</option>
                            </select>
                        </div>
                    </div>
                    <GenreSelector :data="query.data" />
                </div>

                <div
                    v-else-if="query.type == 'emotions'"
                    class="flex flex-row items-center emotions w-full">
                    <div class="front">
                        <div class="type">
                            {{ query.type }}
                        </div>
                        <div class="start">
                            <select v-model="query.start">
                                <option value="HAS">HAS</option>
                                <option value="NOT">NOT</option>
                            </select>
                        </div>
                    </div>
                    <EmotionSelector :data="query.data" />
                </div>

                <div
                    v-else-if="query.type == 'duration'"
                    class="flex flex-row items-center duration w-full">
                    <div class="front">
                        <div class="type">
                            {{ query.type }}
                        </div>
                        <div class="start">
                            <select v-model="query.start">
                                <option value="HAS">HAS</option>
                                <option value="NOT">NOT</option>
                            </select>
                        </div>
                    </div>
                    <DurationSelector :data="query.data" />
                </div>

                <div
                    v-else-if="query.type == 'date'"
                    class="flex flex-row items-center date w-full">
                    <div class="front">
                        <div class="type">
                            {{ query.type }}
                        </div>
                        <div class="start">
                            <select v-model="query.start">
                                <option value="HAS">HAS</option>
                                <option value="NOT">NOT</option>
                            </select>
                        </div>
                    </div>
                    <DateSelector :data="query.data" />
                </div>

                <div class="end">
                    <select
                        v-model="query.end"
                        class="bg-red-500">
                        <option value="AND">AND</option>
                        <option value="OR">OR</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="controls flex flex-col gap-1 w-[50vw] items-center">
            <div class="adders flex flex-row gap-1">
                <div @click="addArtists">Add Artists Field</div>

                <div @click="addGenres">Add Genres Field</div>

                <div @click="addEmotions">Add Emotions Field</div>

                <div @click="addDate">Add Date Field</div>

                <div @click="addDuration">Add Duration Field</div>
            </div>

            <div class="deleters flex flex-row gap-1">
                <div @click="removeLatest">Delete Latest Field</div>

                <div @click="clearAll">Clear All Fields</div>
            </div>
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
    import DateSelector from "./components/DateSelector.vue";
    import DurationSelector from "./components/DurationSelector.vue";
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
            DateSelector,
            DurationSelector,
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
            addDuration() {
                this.search.push({ type: "duration", start: "HAS", data: [], end: "AND" });
            },
            addDate() {
                this.search.push({ type: "date", start: "HAS", data: [], end: "AND" });
            },
            logSearch() {
                console.log(this.search);
            },
            removeLatest() {
                this.search.pop();
            },
            clearAll() {
                this.search = [];
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

<style scoped>
    .type {
        @apply uppercase text-center;
    }

    .artists {
        background-color: #b4656f;
    }

    .genres {
        background-color: #8db1ab;
    }

    .emotions {
        background-color: #587792;
    }

    .date {
        background-color: #372248;
    }

    .duration {
        background-color: #15616d;
    }

    .front {
        @apply flex flex-col items-center gap-2 w-1/6 text-white;
    }

    .adders > div {
        @apply w-40 h-10 bg-green-500 cursor-pointer text-center flex items-center justify-center text-white rounded-xl;
    }

    .deleters > div {
        @apply w-40 h-10 bg-red-500 cursor-pointer text-center flex items-center justify-center text-white rounded-xl;
    }
</style>
