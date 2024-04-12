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
            <select v-model="artistOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
            <div class="w-[10vw] relative h-10">
                <ul
                    class="min-h-10 bg-greeny overflow-auto max-h-[50vh] absolute w-full rounded-md select-none cursor-pointer"
                    @click.stop>
                    <li
                        @click="toggle"
                        class="sticky top-0 h-10 bg-greeny">
                        {{ selectedArtist || "Artists" }}
                    </li>
                    <li
                        v-show="showArtists"
                        class="py-2 border-y-2 sticky top-10 bg-greeny">
                        <input
                            v-model="query"
                            class="w-full h-full bg-white text-greeny py-2 text-sm px-1"
                            type="text"
                            placeholder="Search for an artist"
                            @keyup="filterArtists" />
                    </li>
                    <li
                        v-for="artist in filteredArtists"
                        v-show="showArtists"
                        class="flex items-center cursor-pointer border-b-2 border-dotted py-2"
                        @click="select(artist)">
                        {{ artist }}
                    </li>
                </ul>
            </div>
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
                artists: [],
                filteredArtists: [],
                query: "",
                showArtists: false,
                operators: ["AND", "OR"],
                selectedArtist: "",
                artistOperator: "AND",
            };
        },
        mounted() {
            this.getArtists();
            this.filteredArtists = this.artists;
            this.filterArtists();
            window.addEventListener("click", this.hideArtists);
        },
        beforeDestroy() {
            window.removeEventListener("click", this.hideArtists);
        },
        methods: {
            toggle() {
                this.filterArtists();
                this.showArtists = !this.showArtists;
            },
            hideArtists() {
                this.showArtists = false;
            },
            async getArtists() {
                try {
                    let response = await fetch("https://lyricalysis-v6esf4zmfa-as.a.run.app/artists", {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                        },
                    });

                    if (response.ok) {
                        let data = await response.json();
                        this.artists = data["artists"];
                    }
                } catch (error) {
                    console.error(error);
                }
            },
            updateElement() {
                if (!this.selectedArtist || !this.artistOperator) {
                    return;
                }
                this.data.push(this.artistOperator);
                this.data.push(this.selectedArtist);
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
            filterArtists() {
                if (!this.query) {
                    this.filteredArtists = this.artists;
                    return;
                }

                this.filteredArtists = this.artists.filter((artist) => {
                    return artist.toLowerCase().includes(this.query.toLowerCase());
                });
            },
            select(artist) {
                this.selectedArtist = artist;
                this.showArtists = false;
            },
        },
    };
</script>

<style scoped>
    li {
        @apply min-h-10 text-white px-4 flex items-center;
    }
</style>
