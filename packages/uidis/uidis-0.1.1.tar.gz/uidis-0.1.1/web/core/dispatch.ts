import { JSXElement } from "solid-js"
import { lookup } from "./lookups"
import * as msg from "./msg"

const uiElementByName: Map<string, (props: any) => JSXElement> = new Map()
const uiSchemaByName: Map<string, msg.Struct<any>> = new Map()

export function register<D extends msg.Def>(
    name: string,
    struct: msg.Struct<D>,
    element: (props: msg.Output<msg.Struct<D>>) => JSXElement
) {
    uiElementByName.set(name, element)
    uiSchemaByName.set(name, struct)
}

export async function dispatch(struct: unknown) {
    const [tag, ...rest] = struct as [number, ...any[]]
    const name = await lookup("ui", tag)
    const constructor = uiElementByName.get(name)
    const schema = uiSchemaByName.get(name)
    if (constructor && schema) return constructor(schema.parse(rest))
    throw new Error(`Component ${tag} not found`)
}
