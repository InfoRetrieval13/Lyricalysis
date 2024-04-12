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
        <div class="bg-dredy shadow-lg rounded-md result-section w-[95vw] flex flex-col items-center justify-center gap-2 p-2">
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
                        :src="result.preview"
                        width="156"
                        height="40"
                        frameborder="1"
                        allowtransparency="false"
                        allow="encrypted-media; autoplay=false"
                        class="rounded-md overflow-hidden"></iframe>
                </div>
            </div>
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
                    {
                        track: ["Ordinary Life"],
                        album: ["Starboy (Deluxe)"],
                        track_id: ["09mBPwUMt1TXNtneqvmZZ5"],
                        lyrics: [
                            "Heaven in her mouth, got a hell of a tongue I can feel her teeth when I drive on a bump Fingers letting go of the wheel when I cum Wheel when I cum, wheel when I cum David Carradine, I'ma die when I cum She just givin' head, she don't know what I've done Like I'm James Dean, I'ma die when I'm young Die when I'm young, die when I'm young Heaven knows that I've been told Paid for the life that I chose If I could, I'd trade it all Trade it for a halo And she said that she'll pray for me I said, \"It's too late for me\" 'Cause I think it's safe to say This ain't ordinary life This ain't ordinary life This ain't ordinary life This ain't ordinary life No ordinary life This ain't ordinary life This ain't ordinary life This ain't ordinary life Valhalla is where all the righteous are led Mulholland's where all the damned will be kept Devil on my lap and a cross on my neck Cross on my neck, cross on my neck Over 45, I'ma drift on a bend Do a buck 20, I'ma fly off the edge Everybody said it would hurt in the end Hurt in the end, but I feel nothin' She said that she'll pray for me I said, \"It's too late for me\" 'Cause I think it's safe to say This ain't ordinary life This ain't ordinary life This ain't ordinary life This ain't ordinary life No ordinary life This ain't ordinary life This ain't ordinary life This ain't ordinary life ♪ Angels all singin' in monasteries, yeah My soul is burning in LaFerraris Father, sorry, father, sorry Halos are given to ordinary lives No, but this ain't ordinary life This ain't ordinary life This ain't ordinary life This ain't ordinary life No ordinary life This ain't ordinary life This ain't ordinary life This ain't ordinary life No ordinary life Woah-oh-oh Woah-oh-oh ",
                        ],
                        emotion: ["optimism"],
                        intensity: ["medium"],
                        id: "e5a5e167-55ef-4f3b-af4d-de61d8fb5f84",
                        _version_: 1795847323362787328,
                    },
                    {
                        track: ["Take My Breath - Live"],
                        album: ["Live At SoFi Stadium"],
                        track_id: ["02YlAvsmptN8LisZqrWBIb"],
                        lyrics: [
                            "Oh, take my breath Ooh, yeah Oh, I see you One, two, three Take my breath ♪ Oh, one, two, three Take my breath ♪ Oh, take my breath Ooh, ooh, ooh, ooh Said I saw the fire in your eyes I saw the fire when I look into your eyes You tell me things you wanna try I know temptation is the devil in disguise You risk it all to feel alive, ooh, yeah (You're offering yourself to me like sacrifice) You said you do this all the time Tell me you love me when I bring you to the light So, I say It's like a dream what she feels with me She likes to be on the edge Her fantasy is okay with me Then suddenly, baby says Said Take my breath away And make it last forever, babe Do it now or never, baby Take my breath away Nobody does it better, babe Bring me close to heaven, baby Take my breath ♪ Come on ♪ Oh, oh-oh Oh, oh Take my, take my breath away Nobody does it better, babe Do it now or never, baby, say Take my breath away Nobody does it better, babe Bring me close to heaven, baby Take my breath away, na-na-ooh-ooh Take my breath, yeah Nobody does it better, babe Bring me close to heaven, baby (Take my breath) ",
                        ],
                        emotion: ["ecstasy"],
                        intensity: ["high"],
                        id: "8605b4af-f380-4d85-ab5a-39affc9ef252",
                        _version_: 1795847323364884480,
                    },
                    {
                        track: ["Party Monster - Live"],
                        album: ["Live At SoFi Stadium"],
                        track_id: ["6knNhL3mIaackJvtjmUrfN"],
                        lyrics: [
                            "Los Angeles are you tryna go hard tonight? Let's go ♪ I see, I see, I see I'm good, I'm good, I'm great Know it's been a while, now I'm mixin' up the drink I just need a girl who gon' really understand I just need a girl who gon' really understand I'm good, I'm good, I'm great Know it's been a while, now I'm mixin' up the drank I just need a girl who gon' really understand I just need a girl who gon' really understand And I seen her get rich hittin' the pole I've seen her, I knew she had to know I've seen her take down that tequila Down by the liter, I knew I had to meet her Ooh, she mine, ooh, girl, bump and grind Ooh, she mine, ooh, girl, bump a line Angelina, lips like Angelina Like Angelina (ass shaped like, let's go) Got up, thank the Lord for the day Woke up by a girl, I don't even know her name Woke up by a girl, I don't even know her name I say Got up, thank the Lord for the day Woke up by a girl, I don't even know her name Woke up by a girl, I don't even know her name Paranoid Paranoid Paranoid But I see something in you Paranoid Paranoid Paranoid But I see something in you Paranoid, baby Paranoid, darling Paranoid, baby But I see something in you, girl Paranoid Paranoid I said paranoid, baby But I see something in you Los Angeles! ♪ Oh, oh, oh, oh! Woke up by a girl, I don't even know her name ",
                        ],
                        emotion: ["grief"],
                        intensity: ["high"],
                        id: "3ed2bd84-acfb-4ded-bfc2-21d77615312c",
                        _version_: 1795847323371175936,
                    },
                    {
                        track: ["After Hours - Live"],
                        album: ["Live At SoFi Stadium"],
                        track_id: ["7HK0ZDEsW0lGKKIVYvni2z"],
                        lyrics: [
                            "Ooh, baby I'm fallin' in too deep, oh, no I'm fallin' in too deep, oh, baby I'm fallin' in too deep, oh, so ♪ My darkest hours Girl, I felt so alone inside of this crowded room Different girls on the floor, distractin' my thoughts of you I turned into the man I used to be, to be Put myself to sleep Just so I can get closer to you inside my dreams Didn't wanna wake up 'less you were beside me I just wanted to call you and say, and say Oh, baby Where are you now when I need you most? I'd give it all just to hold you close Sorry that I broke your heart, your heart Never comin' down I was running away from facin' reality Wastin' all of my time out living my fantasies Spendin' money to compensate, compensate 'Cause I want you, baby I be livin' in heaven when I'm inside of you It was simply a blessing wakin' beside you I'll never let you down again, again Oh, baby Where are you now when I need you most? I'd give it all just to hold you close Sorry that I broke your heart, your heart I said, baby I'll treat you better than I did before I'll hold you down and not let you go This time, I won't break your heart, your heart, yeah ♪ I know it's all my fault Made you put down your guard And I know I made you fall Then said you were wrong for me But I lied to you, I lied to you, I lied to you Can't hide the truth, I'd stay with her in spite of you You did some things that you regret, still ride for you 'Cause this house is not a home Without my (baby) (Where are you now when I need you most?) (I gave it all just to hold you close) (Sorry that I broke your heart, your heart) (I said, baby) (I'll treat you better than I did before) (I'll hold you down and not let you go) (This time, I won't break your heart, your heart) No ",
                        ],
                        emotion: ["grief"],
                        intensity: ["high"],
                        id: "c081d9a7-b6e5-43ee-981f-1d9101c8ae83",
                        _version_: 1795847323375370240,
                    },
                    {
                        track: ["Out of Time - Live"],
                        album: ["Live At SoFi Stadium"],
                        track_id: ["6XZ8C5etRn0kiS1wwuW0SO"],
                        lyrics: [
                            "Los Angeles, how the fuck y'all feelin' tonight Look how beautiful you look Look how gorgeous you look tonight And you sound beautiful too, 'cause I just heard you a few seconds ago So, I need you to help me out on this next song, you hear me? Let's go The last few months, I've been workin' on me, baby There's so much trauma in my life I've been so cold to the ones who loved me, baby I look back now and I realize And I remember when I held you You begged me with your drowning eyes to stay And I regret I didn't tell you Now, I can't keep you from loving him You made up your mind Say I love you, girl, but I'm out of time Say I'm there for you, but I'm out of time Say that I'll care for you, but I'm out of time Said I'm too late to make you mine, out of time If he mess up just a little Baby, you know my line If you don't trust him a little Then come right back, girl, come right back Give me one chance, just a little Baby, I'll treat you right And I'll love you like I shoulda loved you all the time And I remember when I held you You begged me with your drowning eyes to stay And I regret I didn't tell you Now, I can't keep you from loving him You made up your mind Say I love you, girl, but I'm out of time Say I'm there for you, but I'm out of time Say that I'll care for you, but I'm out of time Said I'm too late to make you mine, out of time Oh, singin' (out of time) Oh, Los Angeles, oh you look so beautiful tonight, look at you (out of time) Oh, say baby, oh (out of time) Too late to make you mine, out of time (Out of time) (Out of time) Oh, baby, oh, no, no, no ",
                        ],
                        emotion: ["love"],
                        intensity: ["medium"],
                        id: "12a492b1-6b34-4dc2-a632-61ce1fbc44de",
                        _version_: 1795847323378515968,
                    },
                    {
                        track: ["Less Than Zero - Live"],
                        album: ["Live At SoFi Stadium"],
                        track_id: ["0ijIG2j6oRSMDk5Zp91xXt"],
                        lyrics: [
                            "Are you there? Let's g— Remember I was your hero, yeah, yeah, yeah, yeah, yeah I'd wear your heart like a symbol I couldn't save you from my darkest truth of all Yeah, yeah, yeah, yeah, I know I'll always be less than zero Oh, yeah You tried your best with me, I know I couldn't face you with my darkest truth of all You know, you know, you know One, two, one, two, three, let's go (I can't get it) Out of my head No, I can't shake this feeling that crawls in my bed I try to hide it, but I know you know me I try to fight it, but I'd rather be free Oh-oh Oh, yeah Can we meet in the middle? (Oh, oh no) 'Cause you were just like me before Now you'd rather leave me than to watch me die in your arms, oh You ready, you ready, you ready One, two, one, two, three, let's go (I can't get it) Out of my head No, I can't shake this feeling that crawls in my bed I try to hide it, but I know you know me I try to fight it, but I'd rather be free LA make some motherfucking noise! ♪ I can't get it out of my head No, I can't shake this feeling that crawls in my bed I try to hide it, but I know you know me I try to fight it, but I'd rather be free Oh, oh, oh baby I said, one, two, three, sing I can't get it out of my (head) No, I can't shake this feeling that crawls in my bed I try to hide it, but I know you know me I try to fight it, but I'd rather be free Oh, yeah I'll always be less than zero Yeah You tried your best with me, I know ",
                        ],
                        emotion: ["apprehension"],
                        intensity: ["low"],
                        id: "140e7fd9-1a63-4c09-84d1-a8b5c887490c",
                        _version_: 1795847323380613120,
                    },
                    {
                        track: ["How Do I Make You Love Me? - Sebastian Ingrosso & Salvatore Ganacci Remix"],
                        album: ["Dawn FM (Alternate World)"],
                        track_id: ["2urqWNGpjl07PLAafoa5nT"],
                        lyrics: [
                            "I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine Forget 'bout what your daddy said I'll teach you how to shine ♪ How do I make you love me? I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine How do I make you love me? I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine And I can see the real you, girl You don't have to hide Forget 'bout what your daddy said I'll teach you how to shine ♪ How do I make you love me? I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And how do I make you love me? I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach you how to shine And I'll teach- How do I make you love me? ",
                        ],
                        emotion: ["joy"],
                        intensity: ["medium"],
                        id: "617f1404-bc2e-4af7-b0a1-e755ba1b60ea",
                        _version_: 1795847323383758848,
                    },
                    {
                        track: ["Try Me"],
                        album: ["My Dear Melancholy,"],
                        track_id: ["4ppTAJUbNXELZcoUaL90wo"],
                        lyrics: [
                            "Any time is the time Any time for you to get my call, baby (So, baby) Are you alone, baby? If he ain't around, pick up your phone, baby Whoa Can you try me? Try me? Once you put your pride aside You can notify me, -fy me You're the best I ever had Baby girl, remind me, -mind me Let me know if it's on And you know where to find me, find me Having thoughts you never had, yeah I didn't know you were down for him finding out I thought you had some kind of love for your man Well, I'm not tryna break up something You've been workin' out, you've been steady But I'm ready to go all the way if you let me, don't you tempt me You're lookin' good since the last time I looked at you It might have been, been about a couple months But I just got the picture that you texted to me You ain't steady, you look ready to go all the way If you let me take you down on me Can you try me? Try me? (Oh) Once you put your pride aside You can notify me, -fy me (Hey) You're the best I ever had Baby girl, remind me, -mind me Let me know if it's on And you know where to find me, find me (Hey) Having thoughts you never had, yeah Can you try me? Try me? (Hey) Once you put your pride aside You can notify me, -fy me You're the best I ever had Baby girl, remind me, -mind me (Hey) Let me know if it's on (Let me know) And you know where to find me find me (Hey) Having thoughts you never had, yeah ♪ Better try me Don't you mess with me Don't you mess with me The way I kissed your scars The way I fixed your heart, oh Don't you miss me, babe? Don't you miss me, babe? ",
                        ],
                        emotion: ["love"],
                        intensity: ["medium"],
                        id: "8319b157-73ab-4d28-ab18-ed3efaa465ad",
                        _version_: 1795847323386904576,
                    },
                ],
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
        async mounted() {
            await this.updateResults();
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
            async searchFor() {
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
                    let response = await fetch("https://lyricalysis-v6esf4zmfa-as.a.run.app/search", {
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
            async getTrackDetails(track_id) {
                try {
                    let response = await fetch(`https://lyricalysis-v6esf4zmfa-as.a.run.app/get_details/${track_id}`, {
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
                for (let i = 0; i < this.results.length; i++) {
                    let data = await this.getTrackDetails(this.results[i].track_id);
                    this.results[i].url = data.url;
                    this.results[i].name = data.name;
                    this.results[i].preview = data.preview_url;
                    this.results[i].image = data.image;
                    this.results[i].album = this.results[i].album[0];
                    this.results[i].lyrics = this.results[i].lyrics[0];
                }
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
