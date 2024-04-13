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

        <div class="drop w-[20vw] flex items-start justify-center gap-2">
            <select v-model="intensityBoolOperator">
                <option
                    v-for="operator in boolOperators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
            <select v-model="intensityOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>

            <select v-model="selectedIntensity">
                <option
                    value=""
                    disabled
                    selected>
                    Intensity
                </option>
                <option
                    v-for="intensity in intensities"
                    :key="intensity"
                    :value="intensity">
                    {{ intensity }}
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
        name: "IntensitySelector",
        props: { data: Array },
        data() {
            return {
                operators: ["Less Than / Equals", "More Than / Equals"],
                boolOperators: ["AND", "OR"],
                intensities: [1, 2, 3],
                selectedIntensity: "",
                intensityOperator: "More Than / Equals",
                intensityBoolOperator: "AND",
            };
        },
        methods: {
            updateElement() {
                if (!this.selectedIntensity || !this.intensityOperator || !this.intensityBoolOperator) {
                    return;
                }
                this.data.push(this.intensityBoolOperator);
                this.data.push(`${this.intensityOperator} ${this.selectedIntensity}`);
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
