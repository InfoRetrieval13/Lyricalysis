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

        <div class="drop w-[15vw] flex items-start justify-between gap-2">
            <select v-model="dateBoolOperator">
                <option
                    v-for="operator in boolOperators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
            <select v-model="dateOperator">
                <option
                    v-for="operator in operators"
                    :key="operator"
                    :value="operator">
                    {{ operator }}
                </option>
            </select>
            <select v-model="selectedMonth">
                <option
                    v-for="month in months"
                    :key="month"
                    :value="month">
                    {{ month }}
                </option>
            </select>

            <select v-model="selectedYear">
                <option
                    v-for="year in years"
                    :key="year"
                    :value="year">
                    {{ year }}
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
        name: "DateSelector",
        props: { data: Array },
        data() {
            return {
                months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                years: Array.from({ length: 50 }, (_, i) => new Date().getFullYear() - i),
                operators: ["Earlier than", "Later than"],
                boolOperators: ["AND", "OR"],
                selectedMonth: "",
                selectedYear: "",
                dateOperator: "",
                dateBoolOperator: "",
            };
        },
        methods: {
            updateElement() {
                if (!this.selectedMonth || !this.selectedYear || !this.dateOperator || !this.dateBoolOperator) {
                    return;
                }
                this.data.push(this.dateBoolOperator);
                this.data.push(`${this.dateOperator} ${this.selectedMonth} ${this.selectedYear}`);
            },
            removeElement() {
                this.data.pop();
                this.data.pop();
            },
            applyClass(index) {
                let styles = ["border-2", "px-4"];
                if (index % 2 == 1) {
                    styles.push("border-green-500", "bg-green-100");
                } else {
                    styles.push("border-blue-500", "bg-blue-100");
                }
                return styles;
            },
        },
    };
</script>
