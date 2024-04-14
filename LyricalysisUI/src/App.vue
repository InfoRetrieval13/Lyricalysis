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
        <div class="bg-dredy shadow-lg rounded-md result-section w-[95vw] flex flex-col items-center justify-center gap-2 p-2 relative min-h-36">
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
                        <h1 class="text-2xl font-bold text-whitey">{{ result.name }}</h1>
                        <div class="text-xl font-inter font-semibold text-violet">
                            <span v-for="artist in result.artists">{{ artist }}</span>
                        </div>
                        <div class="text-sm">Released: {{ result.release_date[0].substring(0, 10) }}</div>
                        <div class="text-sm">Duration: {{ Math.floor(result.duration / 60) }} minutes {{ result.duration % 60 }} seconds</div>
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
                        album: ["2 days into college"],
                        track: ["2 days into college"],
                        track_id: ["1v4m9GLt7lpFM5iOvwQZrU"],
                        lyrics: [
                            "I'm two days into college and I'm three lectures behind There's this guy, let's name him Colin He says he wants to be mine But it doesn't really sit with me quite right 'Cause he doesn't really like the things I like And I keep accidentally locking myself out of my dorm in the middle of the night I wake up kinda wired and I wake up kinda cold And I wake up kinda tired but I'll just sleep in when I'm old See I don't like breaking rules but don't like doing as I'm told So I just float around and keep my head down And hope my life unfolds And everybody's telling me that I'm doing so well I try to trust them, honestly, I find it hard to tell If I need work or I need rest To try my best, to try my best To tell myself, I say out loud \"It's fine, I'll figure it all out\" I tend to forget, I'm still only quite young In a way, this life of mine has only just begun I've got time I've got time I'm two days into college with a busy, busy mind That guy that we named Colin, he's so handsome, he's so kind My friends tell me I'm crazy, say I'll take it way too far 'Cause I told him that it's over 'cause he doesn't play guitar I'm only two days into college and my bedroom is a mess There's just so much that I want to do that I have not done yet There's just so much that I want to say and far too little breath Oh my mind, it runs so far away, it's easy to forget That to everybody else it looks like I'm doing so well I try to see it, honestly, I find it hard to tell If I've done wrong or I've done right I need a good night's sleep tonight They said, \"Go out\", I said, \"Alright\" I think I won't, I maybe might I probably should just take it slow I'll be all good, but God I know The one thing that's important above everything else Is to learn not to put all this heavy pressure on myself I try believe it when I say \"If it's meant to happen, it'll happen anyway\" I'll be fine I've got time I've got time That's where I'm at, to be honest Just two days Two days into college ",
                        ],
                        duration: ["168"],
                        genre: ['["pop"]'],
                        release_date: ["2023-12-08T00:00:00Z"],
                        explicit: [false],
                        artists: ["Aimee Carty"],
                        url: ["https://open.spotify.com/track/1v4m9GLt7lpFM5iOvwQZrU"],
                        name: ["2 days into college"],
                        preview_url: ["https://p.scdn.co/mp3-preview/577341e410b873f153a6fcc225bffd84b8679399?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b273b1d199f12f84981c4572fb1f"],
                        emotion: ["hope"],
                        intensity: ["3"],
                        id: "247d68a9-faa5-4ad5-b3da-8dd604221593",
                        _version_: 1796230336435191811,
                    },
                    {
                        album: ["hyacinth"],
                        track: ["hyacinth"],
                        track_id: ["6jeYsCtClMoL9MjhNFx8mo"],
                        lyrics: [
                            "One rainy day I found a box full of letters and photos Came across a pretty face I used to know Said hello to the camera Burned every picture so I would Never have to remember what I had was good I've been looking for more than just this Past the mirror, beyond the abyss Tell me fairy tales still exist I want to be Ephemeral, our lives passing by on Earth In comfort do we live with all our flaws Imagine if you could see yourself the way I see you, could we leave to love again? ♪ Walked a busy street A doll stuffed with ashes and pipe dreams Held in by purple seams no one can see, 'cause My skin is sewn by patchwork Words of a song on each shirt Who'd understand me, be willing to accept my quirks? I've been searching for so many days Tryna shoulder the joy and the pain If I could let go of the shame Would I be Ephemeral, our lives passing by on Earth In comfort do we live with all our flaws Imagine if you could see yourself the way I see you Could we learn to love again? (Could we learn to love again?) ",
                        ],
                        duration: ["216"],
                        genre: ["otacore"],
                        release_date: ["2024-02-14T00:00:00Z"],
                        explicit: [false],
                        artists: ["StreamBeats Originals, LilyPichu"],
                        url: ["https://open.spotify.com/track/6jeYsCtClMoL9MjhNFx8mo"],
                        name: ["hyacinth"],
                        preview_url: ["https://p.scdn.co/mp3-preview/f96d2c6c8d752f511b4967f4cc77a9985f3f1428?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b273634da251af2e4010b007c160"],
                        emotion: ["remorse"],
                        intensity: ["2"],
                        id: "f4d8b894-2604-4044-8c84-9e923497a22a",
                        _version_: 1796230333184606208,
                    },
                    {
                        album: ["Nursery Rhymes by CoComelon"],
                        track: ["Baby Shark"],
                        track_id: ["7zD97mcPo9fng0aJqUhFvd"],
                        lyrics: [
                            "Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark, doo, doo, doo, doo, doo, doo Baby shark Mommy shark, doo, doo, doo, doo, doo, doo Mommy shark, doo, doo, doo, doo, doo, doo Mommy shark, doo, doo, doo, doo, doo, doo Mommy shark Daddy shark, doo, doo, doo, doo, doo, doo Daddy shark, doo, doo, doo, doo, doo, doo Daddy shark, doo, doo, doo, doo, doo, doo Daddy shark Grandma shark, doo, doo, doo, doo, doo, doo Grandma shark, doo, doo, doo, doo, doo, doo Grandma shark, doo, doo, doo, doo, doo, doo Grandma shark Grandpa shark, doo, doo, doo, doo, doo, doo Grandpa shark, doo, doo, doo, doo, doo, doo Grandpa shark, doo, doo, doo, doo, doo, doo Grandpa shark Let's go play, doo, doo, doo, doo, doo, doo Let's go play, doo, doo, doo, doo, doo, doo Let's go play, doo, doo, doo, doo, doo, doo Let's go play Run away, do, do, do-do, do-do Run away, do, do, do-do, do-do Run away, do, do, do-do, do-do Run away Hungry sharks, do, do, do-do, do-do Hungry sharks, do, do, do-do, do-do Hungry sharks, do, do, do-do, do-do Hungry sharks Feed the sharks, do, do, do-do, do-do Feed the sharks, do, do, do-do, do-do Feed the sharks, do, do, do-do, do-do Feed the shark It's the end, do, do, do-do, do-do It's the end, do, do, do-do, do-do It's the end, do, do, do-do, do-do It's the end ",
                        ],
                        duration: ["127"],
                        genre: ["children's music, nursery, preschool children's music"],
                        release_date: ["2021-01-08T00:00:00Z"],
                        explicit: [false],
                        artists: ["CoComelon"],
                        url: ["https://open.spotify.com/track/7zD97mcPo9fng0aJqUhFvd"],
                        name: ["Baby Shark"],
                        preview_url: ["https://p.scdn.co/mp3-preview/549be7417c775d68366fe86a52f2362d1d35f06f?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b2734a98c14e3f802b3a2357ce23"],
                        emotion: ["ecstasy"],
                        intensity: ["3"],
                        id: "9d298669-e6f6-452a-b324-22d6fc481930",
                        _version_: 1796230700896092163,
                    },
                    {
                        album: ["Top of 2023"],
                        track: ["Cupid - Twin Ver."],
                        track_id: ["2v36kKQQ1qcO963z3EwGYk"],
                        lyrics: [
                            "La, la, la, la-la-la La, la-la-la-la, la-la-la A hopeless romantic all my life Surrounded by couples all the time I guess I should take it as a sign (Oh, why? Oh, why? Oh, why? Oh, why?) I'm feeling lonely (lonely) Oh, I wish I'd find a lover that could hold me (hold me) Now I'm crying in my room So skeptical of love (say what you say, but I want it more) But still I want it more, more, more I gave a second chance to Cupid But now I'm left here feeling stupid (oh, oh-oh, oh-oh-oh) Oh, the way he makes me feel that love isn't real Cupid is so dumb (oh, oh, oh) I look for his arrows every day (ah) I guess he got lost or flew away (ah) Waiting around is a waste (waste) Been counting the days since November Is loving as good as they say? (Ah, ah) Now I'm so lonely (lonely) Oh, I wish I'd find a lover that could hold me (hold me) Now I'm crying in my room So skeptical of love (say what you say, but I want it more) But still I want it more, more, more I gave a second chance to Cupid But now I'm left here feeling stupid (oh, oh-oh, oh-oh-oh) Oh, the way he makes me feel that love isn't real Cupid is so dumb (oh, oh, oh) (Oh-oh) (Oh, oh, oh-oh, oh-oh-oh-oh-oh) ♪ Cupid is so dumb (oh, oh, oh) Hopeless girl is seeking Someone who will share this feeling I'm a fool A fool for love, a fool for love I gave a second chance to Cupid But now I'm left here feeling stupid (oh, oh-oh, oh-oh-oh) Oh, the way he makes me feel that love isn't real Cupid is so dumb (oh, oh, oh) I gave a second chance to Cupid (hopeless girl) But now I'm left here feeling stupid (is seeking someone who will share this feeling) Oh, the way he makes me feel that love isn't real (I'm a fool, a fool for love) Cupid is so dumb (a fool for love) (oh, oh, oh) ",
                        ],
                        duration: ["174"],
                        genre: ["singer-songwriter pop"],
                        release_date: ["2023-11-16T00:00:00Z"],
                        explicit: [false],
                        artists: ["FIFTY FIFTY"],
                        url: ["https://open.spotify.com/track/2v36kKQQ1qcO963z3EwGYk"],
                        name: ["Cupid - Twin Ver."],
                        preview_url: ["https://p.scdn.co/mp3-preview/3a7021f5109c12e4ddfd4ed25ad68cab367400a9?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b2737494e5c7c69e5792168c4928"],
                        emotion: ["sadness"],
                        intensity: ["2"],
                        id: "916b7d75-78ad-485b-bed2-f2be7c4aaa4d",
                        _version_: 1796230332145467392,
                    },
                    {
                        album: ["happy"],
                        track: ["happy"],
                        track_id: ["0exExEyKJnVIwgF8MyHVNP"],
                        lyrics: [
                            "I wanna stay inside forever In that worn-out yellow sweater The warmth I used to feel is still there (still there...) Heavy sighs like clouds surround me Why do they feel so lonely? I can't pretend to care I'm trying to be happy I'm trying to find a way in this unrelenting world Where I promised that I would stay I'll figure it out, then you'll see I'm everything I ever claimed to be Smile through the dark, to the sky, laugh away Never thought I'd put my phone down Suffocating in a bubble, who's wearing the crown? Everyone's looking for the next big thing While I'm still so lost in a closing ring of faces (the faceless) The shameless (a sad mess) Constantly walking an endless road to the moon, to the stars And I hope to God you get far An eternity's too long to stay on the stage When will I turn the next page? Let me stay inside forever In that worn-out yellow sweater When will the colors fade? This pretty, pretty palette of dull shades What's the definition of a good friend? It's hard to tell in this mad race to the end Can I live so unafraid? I'm trying to be happy I'm trying to find a way in this unrelenting world Where I promised that I would stay I'll figure it out, then you'll see I'm everything I ever claimed to be Smile through the dark, to the sky, laugh away I'm trying to be happy (happy...) ",
                        ],
                        duration: ["216"],
                        genre: ["otacore"],
                        release_date: ["2022-08-21T00:00:00Z"],
                        explicit: [false],
                        artists: ["LilyPichu"],
                        url: ["https://open.spotify.com/track/0exExEyKJnVIwgF8MyHVNP"],
                        name: ["happy"],
                        preview_url: ["https://p.scdn.co/mp3-preview/82e742abdf16e7fa9445db5879afd596515c9b7d?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b2732594801003eb0053c25452ad"],
                        emotion: ["pensiveness"],
                        intensity: ["1"],
                        id: "de0a34d8-9c42-4dd4-8065-818ba99d08fa",
                        _version_: 1796230333184606215,
                    },
                    {
                        album: ["Hollywood's Bleeding"],
                        track: ["Sunflower - Spider-Man: Into the Spider-Verse"],
                        track_id: ["0RiRZpuVRbi7oqRdSMwhQY"],
                        lyrics: [
                            "Ayy, ayy, ayy, ayy (ooh) Ooh, ooh, ooh, ooh (ooh)  Ayy, ayy Ooh, ooh, ooh, ooh ♪ Needless to say, I keep her in check She was a bad-bad, nevertheless (yeah) Callin' it quits now, baby, I'm a wreck (wreck) Crash at my place, baby, you're a wreck (wreck) Needless to say, I'm keeping her in check She was all bad-bad, nevertheless Callin' it quits now, baby, I'm a wreck Crash at my place, baby, you're a wreck Thinkin' in a bad way, losin' your grip Screamin' at my face, baby, don't trip Someone took a big L, don't know how that felt Lookin' at you sideways, party on tilt Ooh-ooh-ooh Some things you just can't refuse She wanna ride me like a cruise And I'm not tryna lose Then you're left in the dust Unless I stuck by ya You're the sunflower I think your love would be too much Or you'll be left in the dust Unless I stuck by ya You're the sunflower You're the sunflower Every time I'm leavin' on you (ooh) You don't make it easy, no (no, no) Wish I could be there for you Give me a reason to, oh (oh) Every time I'm walkin' out I can hear you tellin' me to turn around Fightin' for my trust and you won't back down Even if we gotta risk it all right now, oh (now) I know you're scared of the unknown ('known) You don't wanna be alone (alone) I know I always come and go (and go) But it's out of my control And you'll be left in the dust Unless I stuck by ya You're the sunflower I think your love would be too much Or you'll be left in the dust Unless I stuck by ya You're the sunflower You're the sunflower (yeah) ",
                        ],
                        duration: ["157"],
                        genre: ["pop, r&b, rap"],
                        release_date: ["2019-09-06T00:00:00Z"],
                        explicit: [false],
                        artists: ["Post Malone, Swae Lee"],
                        url: ["https://open.spotify.com/track/0RiRZpuVRbi7oqRdSMwhQY"],
                        name: ["Sunflower - Spider-Man: Into the Spider-Verse"],
                        preview_url: ["https://p.scdn.co/mp3-preview/3c0788c6aba94192edcb497d9a02075bf76c5400?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b2739478c87599550dd73bfa7e02"],
                        emotion: ["love"],
                        intensity: ["2"],
                        id: "10f5d45b-2621-4f83-bc2d-c3e598e25dc5",
                        _version_: 1796228347670298624,
                    },
                    {
                        album: ["METRO BOOMIN PRESENTS SPIDER-MAN: ACROSS THE SPIDER-VERSE (SOUNDTRACK FROM AND INSPIRED BY THE MOTION PICTURE / DELUXE EDITION)"],
                        track: ["Self Love (Spider-Man: Across the Spider-Verse) (Metro Boomin & Coi Leray)"],
                        track_id: ["2dHNeQOgkDxcheR65nUg7p"],
                        lyrics: [
                            "(Metro) Yeah Hmm Oh my, she's a long way from suburban towns Came to the city for the love, got her hurtin' now Oh my, she's a long way from suburban town Long way, really long way from suburbia Small town love, fall down love, not medicated Drink too much, think too much, thoughts drownin' me I'm too high, please don't cry, stop doubtin' me You don't know love, you just show love, stop downin' me Self-love, he don't love himself, tryna love me Cuff me, told the truth to him, he don't trust me Self-love, he don't love himself, tryna love me Cuff me, told the truth to him, he don't trust me Oh my, she's a long way from suburban towns Came to the city for the love, got her hurtin' now Oh my, she's a long way from suburban town Long way, really long way from suburbia Big dreams, yeah (yo), big screams, yeah (oh, yo) She's impressionable Hate to see, yeah (whoa), money scheme, yeah (whoa) Livin' questionable My friends drive (yo), new beamers (yo) Drop top convertibles Love hangin' out, say you hate it now Feelin' introvertical Self-love, he don't love himself, tryna love me Cuff me, told the truth to him, he don't trust me Self-love, he don't love himself, tryna love me Cuff me, told the truth to him, he don't trust me Oh my, she's a long way from suburban towns Came to the city for the love, got her hurtin' now Oh my, she's a long way from suburban town Long way, really long way from suburbia ♪ Self-love, he don't love himself, tryna love me Cuff me, told the truth to him, he don't trust me Self-love, he don't love himself, tryna love me Cuff me, told the truth to him, he don't trust me Oh my, she's a long way from suburban towns Came to the city for the love, got her hurtin' now Oh my, she's a long way from suburban town Long way, really long way from suburbia In every other universe Gwen Stacy falls for Spider-Man  And in every other universe it doesn't end well Well, it's a first time for everything, right? ",
                        ],
                        duration: ["189"],
                        genre: ["hip hop, rap"],
                        release_date: ["2023-06-05T00:00:00Z"],
                        explicit: [false],
                        artists: ["Metro Boomin, Coi Leray"],
                        url: ["https://open.spotify.com/track/2dHNeQOgkDxcheR65nUg7p"],
                        name: ["Self Love (Spider-Man: Across the Spider-Verse) (Metro Boomin & Coi Leray)"],
                        preview_url: ["https://p.scdn.co/mp3-preview/a3b8fa8de995cd1d96b3fbdb0947e4291bd89f4a?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b2734a3cdc1e547b3d275d97cff8"],
                        emotion: ["ecstasy"],
                        intensity: ["3"],
                        id: "1651314a-cf82-4c14-bd59-1f4e8e1f6300",
                        _version_: 1796228348273229826,
                    },
                    {
                        album: ["Soirée d'été : Summer Hits Mix 2022"],
                        track: ["Uptown Girl"],
                        track_id: ["5bEE4NPhhkIfqn6Po0TTIB"],
                        lyrics: [
                            "Uptown girl She's been living in her uptown world I bet she's never had a backstreet guy I bet her momma never told her why I'm gonna try for an uptown girl She's been living in her white-bred world As long as anyone with hot blood can And now she's looking for a downtown man That's what I am And when she knows what She wants from her time And when she wakes up And makes up her mind She'll see I'm not so tough Just because I'm in love with an uptown girl You know I've seen her in her uptown world She's getting tired of her high-class toys And all her presents from her uptown boys She's got a choice Oh, oh, oh, oh Oh, oh, oh, oh Oh, oh, oh, oh Oh, oh, oh, oh Uptown girl You know I can't afford to buy her pearls But maybe someday when my ship comes in She'll understand what kind of guy I've been And then I'll win And when she's walking She's looking so fine And when she's talking She'll say that she's mine She'll say I'm not so tough Just because I'm in love With an uptown girl She's been living in her white-bred world As long as anyone with hot blood can And now she's looking for a downtown man That's what I am Oh, oh, oh, oh Oh, oh, oh, oh Oh, oh, oh, oh Oh, oh, oh, oh ♪ Uptown girl She's my uptown girl You know I'm in love With an uptown girl My uptown girl You know I'm in love With an uptown girl My uptown girl You know I'm in love With an uptown girl My uptown girl You know I'm in love With an uptown girl ",
                        ],
                        duration: ["195"],
                        genre: ["modern alternative rock, modern rock, pop"],
                        release_date: ["2022-07-02T00:00:00Z"],
                        explicit: [false],
                        artists: ["Billy Joel"],
                        url: ["https://open.spotify.com/track/5bEE4NPhhkIfqn6Po0TTIB"],
                        name: ["Uptown Girl"],
                        preview_url: ["https://p.scdn.co/mp3-preview/ff17fd8ca6e737fa2d71a78305deeb6ee512b768?cid=162b7dc01f3a4a2ca32ed3cec83d1e02"],
                        image: ["https://i.scdn.co/image/ab67616d0000b27325d1f72611ce3b962e4f9100"],
                        emotion: ["joy"],
                        intensity: ["2"],
                        id: "aa85add5-6428-4c1c-b983-cd1389d34b6d",
                        _version_: 1796230333007396866,
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
                        this.results[i].url = this.results[i].url[0];
                        this.results[i].name = this.results[i].name[0];
                        this.results[i].preview = this.results[i].preview_url[0];
                        this.results[i].image = this.results[i].image[0];
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
