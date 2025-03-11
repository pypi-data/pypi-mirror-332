import { createResource, Show } from "solid-js"
import { register } from "../core/dispatch"
import { resolver } from "../core/lookups"
import * as msg from "../core/msg"

export const Outlined = "outlined"
export const Rounded = "rounded"
export const Sharp = "sharp"

const IconStyles = [Outlined, Rounded, Sharp] as const
const IconStyle = msg.enums(IconStyles)

export const IconStruct = msg.def("Icon", {
    code: msg.number,
    style: msg.nullable(IconStyle),
})

export const Icon = (icon: msg.Output<typeof IconStruct>) => {
    const [name] = createResource(resolver("icon", icon.code))
    return (
        <Show when={name()}>
            <span class={`material-symbols-${icon.style ?? Outlined} icon`}>
                {name()}
            </span>
        </Show>
    )
}

export const AppIcon = (icon: { name: string }) => (
    <span class={`material-symbols-${Outlined} icon`}>{icon.name}</span>
)

export const DefaultIcon = (props: { code?: number | null }) =>
    props.code ? <Icon code={props.code} style={null} /> : <></>

register("Icon", IconStruct, Icon)
