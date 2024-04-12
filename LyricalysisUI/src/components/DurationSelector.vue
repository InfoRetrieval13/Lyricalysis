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
            <select v-model="durationBoolOperator">
                <option
                    v-for="operator in boolOperators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
            <select v-model="durationOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>

            <select v-model="duration">
                <option
                    value=""
                    disabled
                    selected>
                    Duration
                </option>
                <option
                    v-for="i in durationOptions"
                    :key="i"
                    :value="i">
                    {{ i }}
                </option>
            </select>

            <div class="w-15 h-10 bg-green-500 text-white rounded-md flex items-center justify-center px-2">Seconds</div>
        </div>

        <div class="flex w-[10vw] items-start justify-between gap-2">
            <button @click="updateElement">Add</button>

            <button @click="removeElement">Clear Latest</button>
        </div>
    </div>
</template>
<script>
    export default {
        name: "DurationSelector",
        props: { data: Array },
        data() {
            return {
                operators: ["Shorter Than / Equals", "Longer Than / Equals"],
                boolOperators: ["AND", "OR"],
                duration: "",
                durationOptions: [15, 30, 45, 60, 90, 120, 150, 180, 210, 240, 270, 300, 360, 420, 480, 540, 600],
                durationOperator: "Shorter Than / Equals",
                durationBoolOperator: "AND",
            };
        },
        methods: {
            updateElement() {
                if (!this.duration || !this.durationOperator || !this.durationBoolOperator) {
                    return;
                }
                this.data.push(this.durationBoolOperator);
                this.data.push(`${this.durationOperator} ${this.duration} seconds`);
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
