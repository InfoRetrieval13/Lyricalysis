<template>
    <div class="main w-screen h-screen flex flex-col items-center gap-10">
        <h1 class="text-9xl">Lyricalysis</h1>
        <div
            class="search-bar items-start justify-start w-[95vw] min-h-[10vh] border-b-4 flex flex-wrap"
            style="row-gap: 1rem">
            <div
                v-for="(query, index) in search"
                class="flex items-start w-[31vw] gap-2 ml-2">
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

                <div
                    v-else-if="query.type == 'intensity'"
                    class="flex flex-row items-center intensity w-full">
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
                    <IntensitySelector :data="query.data" />
                </div>

                <div
                    class="end"
                    v-if="query.type != 'explicit'"
                    :class="hideLast(index)">
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

                <div @click="addIntensity">Add Intensity Field</div>
            </div>

            <div class="deleters flex flex-row gap-1">
                <div @click="removeLatest">Delete Latest Field</div>

                <div @click="clearAll">Clear All Fields</div>
            </div>
        </div>

        <div class="explicit">
            <label for="explicit">Include Explicit Songs: </label>
            <select
                name="explicit"
                id="explicit">
                <option value="yes">Yes</option>
                <option value="no">No</option>
                <option value="only">Only</option>
            </select>
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
    import IntensitySelector from "./components/IntensitySelector.vue";
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
            IntensitySelector,
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
            addIntensity() {
                this.search.push({ type: "intensity", start: "HAS", data: [], end: "AND" });
            },
            async logSearch() {
                let searchQuery = JSON.parse(JSON.stringify(this.search));
                for (let elem of searchQuery) {
                    // remove first element of elem.data
                    elem.data.shift();
                }
                // set the end value of the last element to null
                searchQuery[this.search.length - 1].end = null;
                searchQuery.push({ type: "explicit", data: document.getElementById("explicit").value });
                // send the search data to the backend
                try {
                    let response = await fetch("http://localhost:5000/search", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(searchQuery), // Send the JSON data directly
                    });
                    let data = await response.json();
                } catch (error) {
                    console.error(error);
                }
            },
            removeLatest() {
                this.search.pop();
            },
            clearAll() {
                this.search = [];
            },
        },
        computed: {
            hideLast() {
                return (index) => {
                    if (this.search[this.search.length - 1].type != "explicit") {
                        if (index == this.search.length - 1) {
                            return "invisible";
                        }
                        return "";
                    } else {
                        if (index == this.search.length - 2) {
                            return "invisible";
                        }
                        return "";
                    }
                };
            },
        },
    };
</script>

<style>
    button {
        @apply w-40 h-10 bg-blue-500 text-white rounded-xl;
    }

    select {
        @apply min-w-20 h-10 bg-green-500 text-white px-4 rounded-md;
    }
</style>

<style scoped>
    .type {
        @apply uppercase text-center font-inter font-semibold select-none;
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

    .intensity {
        background-color: #f4a261;
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
