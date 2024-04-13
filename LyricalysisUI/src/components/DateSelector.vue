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
                    value=""
                    disabled
                    selected>
                    Month
                </option>
                <option
                    v-for="month in months"
                    :key="month"
                    :value="month">
                    {{ month }}
                </option>
            </select>

            <select v-model="selectedYear">
                <option
                    value=""
                    disabled
                    selected>
                    Year
                </option>
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
                operators: ["Earlier Than / Equals", "Later Than / Equals"],
                boolOperators: ["AND", "OR"],
                selectedMonth: "",
                selectedYear: "",
                dateOperator: "Later Than / Equals",
                dateBoolOperator: "AND",
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
