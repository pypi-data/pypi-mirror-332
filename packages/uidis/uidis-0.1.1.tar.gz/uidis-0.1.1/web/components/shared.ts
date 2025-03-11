import { z } from "zod"

const ColorTagName = [null, "primary", "secondary", "tertiary", "error"]

export const ColorName = z.number().transform(tag => ColorTagName[tag])
export const Color = ColorName.transform(name =>
    name ? `var(--md-sys-color-${name})` : ""
)
export const ColorContainer = ColorName.transform(name =>
    name ? `var(--md-sys-color-${name}-container)` : ""
)
export const ColorOnContainer = ColorName.transform(name =>
    name ? `var(--md-sys-color-on-${name}-container)` : ""
)
