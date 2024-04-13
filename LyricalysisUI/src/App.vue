<template>
    <div class="main w-screen min-h-screen flex flex-col items-center gap-10 bg-dbluey py-5">
        <h1 class="text-9xl font-lora text-whitey">Lyricalysis</h1>
        <div class="w-screen flex flex-col items-center gap-10 search-section">
            <div
                class="search-bar items-start justify-start w-[95vw] min-h-[10vh] shadow-2xl rounded-md bg-grey flex flex-wrap"
                style="row-gap: 1rem">
                <div
                    class="text-8xl flex items-center justify-start px-10 w-full h-[10vh] select-none font-roboto text-whitey"
                    v-if="search.length == 0">
                    Search . . .
                </div>
                <div
                    v-for="(query, index) in search"
                    class="flex items-start w-[31vw] gap-2 ml-[0.5vw] my-[0.5vw] queries">
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
                            class="bg-redy">
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

                    <div @click="addDate">Add Date Field</div>

                    <div @click="addDuration">Add Duration Field</div>

                    <div @click="addEmotions">Add Emotions Field</div>

                    <div @click="addIntensity">Add Intensity Field</div>
                </div>

                <div class="deleters flex flex-row gap-1">
                    <div @click="removeLatest">Delete Latest Field</div>

                    <div @click="clearAll">Clear All Fields</div>
                </div>
            </div>

            <div class="explicit text-whitey gap-2 flex items-center">
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
                <button @click="searchFor">Search</button>
            </div>
        </div>
        <div class="bg-dredy shadow-lg rounded-md result-section w-[95vw] flex flex-col items-center justify-center gap-2 p-2 relative">
            <div class="absolute -top-7 right-2 text-whitey">
                {{ searchTime }}
            </div>
            <div
                v-for="result in results"
                class="result-item flex items-center justify-between song-info p-4 rounded-md shadow-md w-full">
                <div class="flex items-center w-[15vw]">
                    <img
                        class="w-36 h-36 rounded-md mr-4"
                        :src="result.image"
                        alt="" />
                    <div>
                        <h1 class="text-xl font-bold text-whitey">{{ result.name }}</h1>
                        <h2 class="text-lg text-violet">{{ result.album }}</h2>
                    </div>
                </div>
                <div class="w-[50vw] h-36 flex overflow-auto p-2 shadow-2xl lyrics rounded-md">
                    {{ result.lyrics }}
                </div>

                <div class="w-[10vw] h-36">
                    <div class="text-2xl flex flex-row gap-2">
                        <div class="text-[#E1D89F]">Emotion(s):</div>
                        <span
                            v-for="emotion in result.emotion"
                            class="text-whitey">
                            {{ emotion }}
                        </span>
                    </div>

                    <div class="text-2xl flex flex-row gap-2">
                        <div class="text-[#7293A0]">Intensity:</div>
                        <span class="text-whitey">
                            {{ result.intensity[0] }}
                        </span>
                    </div>
                </div>
                <div class="links h-36 flex flex-row items-center gap-2">
                    <a
                        v-if="v1"
                        :href="result.url"
                        target="_blank">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="100"
                            height="100"
                            fill="#1ed45e"
                            class="bi bi-spotify"
                            viewBox="0 0 16 16">
                            <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.669 11.538a.5.5 0 0 1-.686.165c-1.879-1.147-4.243-1.407-7.028-.77a.499.499 0 0 1-.222-.973c3.048-.696 5.662-.397 7.77.892a.5.5 0 0 1 .166.686m.979-2.178a.624.624 0 0 1-.858.205c-2.15-1.321-5.428-1.704-7.972-.932a.625.625 0 0 1-.362-1.194c2.905-.881 6.517-.454 8.986 1.063a.624.624 0 0 1 .206.858m.084-2.268C10.154 5.56 5.9 5.419 3.438 6.166a.748.748 0 1 1-.434-1.432c2.825-.857 7.523-.692 10.492 1.07a.747.747 0 1 1-.764 1.288" />
                        </svg>
                    </a>
                    <iframe
                        v-if="v1"
                        :src="result.preview"
                        width="156"
                        height="40"
                        frameborder="1"
                        allowtransparency="false"
                        allow="encrypted-media; autoplay=false"
                        class="rounded-md overflow-hidden"></iframe>
                    <iframe
                        v-else
                        style="border-radius: 12px"
                        :src="spotifyEmbedUrl(result.track_id)"
                        width="100%"
                        height="152"
                        frameBorder="0"
                        allowfullscreen=""></iframe>
                </div>
            </div>
        </div>
    </div>
    <Loading
        v-if="isLoading"
        :text="loadingText" />
</template>

<script>
    import ArtistSelector from "./components/ArtistSelector.vue";
    import GenreSelector from "./components/GenreSelector.vue";
    import EmotionSelector from "./components/EmotionSelector.vue";
    import DateSelector from "./components/DateSelector.vue";
    import DurationSelector from "./components/DurationSelector.vue";
    import IntensitySelector from "./components/IntensitySelector.vue";
    import Loading from "./components/Loading.vue";
    export default {
        name: "App",
        data() {
            return {
                isLoading: false,
                loadingText: "Searching...",
                search: [],
                v1: false,
                results: [
                    {
                        track: ["Earned It (Fifty Shades Of Grey)"],
                        album: ["The Highlights (Deluxe)"],
                        track_id: ["5cTYNNvFtfVtRbGj6073U3"],
                        lyrics: [
                            "I'ma care for you ♪ I'ma care for you, you, you, you ♪ You make it look like it's magic (oh, yeah) 'Cause I see nobody, nobody but you, you, you I'm never confused Hey, hey, and I'm so used to being used So I love when you call unexpected 'Cause I hate when the moment's expected So I'ma care for you, you, you I'ma care for you, you, you, you, yeah 'Cause girl, you're perfect You're always worth it And you deserve it The way you work it 'Cause girl, you earned it, yeah Girl, you earned it, yeah You know our love would be tragic (oh, yeah) So you don't pay it, don't pay it no mind, mind, mind We live with no lies Hey, hey, and you're my favorite kind of night So I love when you call unexpected 'Cause I hate when the moment's expected So I'ma care for you, you, you I'ma care for you, you, you, you, yeah 'Cause girl, you're perfect (girl, you're perfect) You're always worth it (always worth it) And you deserve it (and you deserve it) The way you work it (the way you work it) 'Cause girl, you earned it, yeah (earned it) Girl, you earned it, yeah On that lonely night (lonely night) Said it wouldn't be love But we felt the rush (fell in love) It made us believe it was only us (was only us) Convinced we were broken inside, yeah Inside, yeah 'Cause girl, you're perfect (girl, you're perfect) You're always worth it (you're always worth it) And you deserve it (and you deserve it) The way you work it (the way you work it) 'Cause girl, you earned it, yeah (girl, you earned it) Girl, you earned it, yeah (girl, you earned it) ♪ Na-na-na-na Oh, yeah, yeah  'Cause girl, you're perfect The way you work it You deserve it Girl, you deserve it Girl, you earned it, yeah ",
                        ],
                        emotion: ["admiration"],
                        intensity: ["high"],
                        id: "25ddd246-8722-4e33-8b54-2eaa03519977",
                        _version_: 1795847323233812480,
                    },
                    {
                        track: ["Wasted Times"],
                        album: ["The Highlights (Deluxe)"],
                        track_id: ["7tDLiXn8gSZ0KuQubcNVPX"],
                        lyrics: [
                            "Wasted times I spent with someone else She wasn't even half of you Reminiscin' how you felt (Reminiscin' how you felt) And even though you put my life through hell I can't seem to forget 'bout you, 'bout you I want you to myself And now I'm askin', who do you belong to now? Who you give that love to now? Who you pullin' up on? Who you gettin' sprung for now? And what they got that I ain't got? 'Cause I got a lot Don't make me run up on 'em, got me blowin' up their spot 'Cause I ain't got no business catchin' feelings anyway I ain't got no business catchin' feelings, catchin' feelings These girls only want you when you're winnin' (Winnin') But you've been with me from the beginnin' (Ooh, yeah-eah) And I know right now that we're not talkin' (Not talkin') I hope you know this dick is still an option 'Cause I'll beat it up (I'll beat it up, yeah) I'll take my time to learn the way your body functions You were equestrian, so ride it like a champion (I'll beat it) This sex will get you high without no other substance So who do you belong to now? (Who do you belong to now?) Who you give that love to now? (Who you give that love to now?) Who you pullin' up on? Who you gettin' sprung for now? (Who you gettin' sprung for now?) And what they got that I ain't got? 'Cause I got a lot (I got a lot) Don't make me run up on 'em, got me blowin' up their spot 'Cause I ain't got no business catchin' feelings anyway I ain't got no business catchin' feelings (Feelings) (Catchin' feelings) (I ain't got no business catchin' feelings) (I ain't got no business catchin' feelings) (Catchin' fee-fee-fee-fee) (Feelings) (I ain't got no business catchin' feelings) (I ain't got no business catchin' feelings) (Catchin' fee-fee-fee-fee) Wake up I don't wanna wake up I don't wanna wake up If you ain't layin' next to me I don't wanna wake up I don't wanna wake up I don't wanna wake up If you ain't layin' next to me-e-e (On me, me) (On me, oh, I–) (On me, on me, on me) ",
                        ],
                        emotion: ["annoyance"],
                        intensity: ["low"],
                        id: "7735dcc6-1ceb-4ade-a8e2-1dce6bb77548",
                        _version_: 1795847323357544448,
                    },
                ],
                searchTime: "Search Time: 0.000s",
            };
        },
        components: {
            ArtistSelector,
            GenreSelector,
            EmotionSelector,
            DateSelector,
            DurationSelector,
            IntensitySelector,
            Loading,
        },
        async mounted() {
            await this.updateResults();
        },
        methods: {
            spotifyEmbedUrl(track_id) {
                let track = track_id[0];
                return `https://open.spotify.com/embed/track/${track}`;
            },
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
            async searchFor() {
                this.isLoading = true;
                let startTime = new Date();
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
                    let response = await fetch("http://localhost:5000/send_search", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(searchQuery), // Send the JSON data directly
                    });
                    let data = await response.json();
                    this.results = data["docs"];
                    let endTime = new Date();
                    this.searchTime = `Search Time: ${(endTime - startTime) / 1000}s`;
                    await this.updateResults();
                    this.isLoading = false;
                } catch (error) {
                    console.error(error);
                    this.isLoading = false;
                }
            },
            removeLatest() {
                this.search.pop();
            },
            clearAll() {
                this.search = [];
            },
            async getTrackDetails(track_id) {
                try {
                    let response = await fetch(`http://localhost:5000/get_details/${track_id}`, {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                        },
                    });
                    let data = await response.json();
                    return data;
                } catch (error) {
                    console.error(error);
                }
            },
            async updateResults() {
                this.isLoading = true;
                try {
                    for (let i = 0; i < this.results.length; i++) {
                        let data = await this.getTrackDetails(this.results[i].track_id);
                        this.results[i].url = data.url;
                        this.results[i].name = data.name;
                        this.results[i].preview = data.preview_url;
                        this.results[i].image = data.image;
                        this.results[i].album = this.results[i].album[0];
                        this.results[i].lyrics = this.results[i].lyrics[0];
                    }
                } catch (error) {
                    console.error(error);
                }
                this.isLoading = false;
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
    body {
        @apply bg-dbluey;
    }
    button {
        @apply w-40 h-10 bg-bluey text-whitey rounded-xl font-poppins cursor-pointer;
    }

    select {
        @apply min-w-20 h-10 bg-greeny text-whitey px-4 rounded-md font-roboto cursor-pointer;
    }

    /* Hide scrollbar for Chrome, Safari and Opera */
    ::-webkit-scrollbar {
        width: 0px;
        background: transparent; /* make scrollbar transparent */
    }

    /* Hide scrollbar for IE, Edge and Firefox */
    html {
        scrollbar-width: none; /* For Firefox */
        -ms-overflow-style: none; /* For Internet Explorer and Edge */
    }

    body {
        overflow: -moz-scrollbars-none; /* For Firefox */
        -ms-overflow-style: none; /* For Internet Explorer and Edge */
    }
</style>

<style scoped>
    .type {
        @apply uppercase text-center font-roboto font-bold select-none;
    }

    .artists {
        background-color: #ffbf00;
    }

    .genres {
        background-color: #b4ebca;
    }

    .emotions {
        background-color: #e1d89f;
    }

    .date {
        background-color: #bcf4f5;
    }

    .duration {
        background-color: #ffb7c3;
    }

    .intensity {
        background-color: #7293a0;
    }

    .front {
        @apply flex flex-col items-center gap-2 w-1/6 text-violet;
    }

    .adders > div {
        @apply w-40 h-10 bg-greeny cursor-pointer text-center flex items-center justify-center text-whitey rounded-xl;
    }

    .deleters > div {
        @apply w-40 h-10 bg-redy cursor-pointer text-center flex items-center justify-center text-whitey rounded-xl;
    }

    .queries > div {
        @apply rounded-md;
        box-shadow: 0 10px 15px -3px rgba(255, 255, 255, 0.1), 0 4px 6px -2px rgba(255, 255, 255, 0.05);
    }

    .song-info {
        @apply shadow-2xl;
        background: rgba(255, 255, 255, 0.03);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 255, 0.05);
    }

    .lyrics {
        background-color: rgba(88, 85, 99, 0.7);
        backdrop-filter: blur(10px);
    }
</style>
