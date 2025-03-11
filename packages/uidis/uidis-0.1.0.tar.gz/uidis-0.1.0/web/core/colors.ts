import { enums } from "./msg"

export const Colors = ["primary", "secondary", "tertiary", "error"] as const

export const colorName = enums(Colors)

export const color = (input: unknown) =>
    `var(--md-sys-color-${colorName(input)})`

export const colorContainer = (input: unknown) =>
    `var(--md-sys-color-${colorName(input)}-container)`

export const colorOnContainer = (input: unknown) =>
    `var(--md-sys-color-on-${colorName(input)}-container)`
