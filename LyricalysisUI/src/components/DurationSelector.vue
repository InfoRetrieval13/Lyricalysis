<template>
    <div class="w-[24vw] flex-wrap flex flex-col gap-2 items-center shadow-sm rounded-sm py-2">
        <div class="data flex flex-row gap-2 max-w-max flex-wrap items-start justify-start p-2">
            <div
                v-for="(info, index) in data"
                :class="applyClass(index)"
                class="px-4">
                {{ info }}
            </div>
        </div>

        <div class="drop w-[15vw] flex items-start justify-between gap-2">
            <select v-model="durationOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>

            <input
                v-model="duration"
                type="number"
                min="1"
                class="w-20 h-10 bg-green-500 text-white" />

            <select v-model="durationUnit">
                <option
                    v-for="unit in units"
                    :key="unit"
                    :value="unit">
                    {{ unit }}
                </option>
            </select>

            <select v-model="durationBoolOperator">
                <option
                    v-for="operator in boolOperators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
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
        name: "DurationSelector",
        props: { data: Array },
        data() {
            return {
                operators: ["Shorter than", "Longer than"],
                units: ["seconds", "minutes"],
                boolOperators: ["AND", "OR"],
                duration: null,
                durationUnit: "",
                durationOperator: "",
                durationBoolOperator: "",
            };
        },
        methods: {
            updateElement() {
                if (!this.duration || !this.durationUnit || !this.durationOperator || !this.durationBoolOperator) {
                    return;
                }
                this.data.push(`${this.durationOperator} ${this.duration} ${this.durationUnit}`);
                this.data.push(this.durationBoolOperator);
            },
            removeElement() {
                this.data.pop();
                this.data.pop();
            },
            applyClass(index) {
                let styles = ["border-2"];
                if (index % 2 == 0) {
                    styles.push("border-green-500", "bg-green-100");
                } else {
                    styles.push("border-blue-500", "bg-blue-100");
                }
                return styles;
            },
        },
    };
</script>
