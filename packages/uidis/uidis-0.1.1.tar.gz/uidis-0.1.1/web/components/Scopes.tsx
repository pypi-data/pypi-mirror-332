import {
    Accessor,
    createMemo,
    createResource,
    createSignal,
    For,
    Show,
} from "solid-js"
import { DefaultIcon, AppIcon } from "./Icon"
import { Pulse } from "./Pulse"
import { fetchPackageAsync } from "../core/server"

type ItemSchema = [label: string, url: string, icon: number | null]
type ScopeSchema = [
    label: string,
    items: (ScopeSchema | ItemSchema)[],
    icon: number | null
]

type ActiveOnSelection = Map<number, Set<number>>

type NavigationItem = {
    label: string
    icon: number | null
    url: string
    isScope: false
}

type NavigationScope = {
    id: number
    label: string
    icon: number | null
    isScope: true
}

type NavigationBar = {
    id: number
    label: string
    icon: number | null
    items: (NavigationItem | NavigationScope)[]
}

type NavigationState = {
    selection: Accessor<number | null>
    active: Accessor<Set<number>>
    select: (id: number | null) => void
}

function processNavigationStructure(scope: ScopeSchema) {
    const activeOnSelection: ActiveOnSelection = new Map()
    const bars: NavigationBar[] = []

    let idCounter = 0
    const parentIdsStack: number[] = []

    function processScope(scope: ScopeSchema): NavigationBar {
        const [label, items, icon] = scope
        const scopeId = idCounter++

        const parentSet = new Set<number>()
        for (let i = 0; i < parentIdsStack.length; i++) {
            parentSet.add(parentIdsStack[i])
        }

        activeOnSelection.set(scopeId, parentSet)
        const navItems: (NavigationItem | NavigationScope)[] = []
        parentIdsStack.push(scopeId)

        for (let i = 0; i < items.length; i++) {
            const item = items[i]
            if (Array.isArray(item[1])) {
                const nestedScope = item as ScopeSchema
                const nestedNavBar = processScope(nestedScope)
                navItems.push({
                    id: nestedNavBar.id,
                    label: nestedNavBar.label,
                    icon: nestedNavBar.icon,
                    isScope: true,
                })
            } else {
                const [itemLabel, itemUrl, itemIcon] = item as ItemSchema
                navItems.push({
                    label: itemLabel,
                    icon: itemIcon,
                    url: itemUrl,
                    isScope: false,
                })
            }
        }

        parentIdsStack.pop()
        const navBar = {
            id: scopeId,
            label,
            icon: icon,
            items: navItems,
        }

        bars.push(navBar)
        return navBar
    }

    processScope(scope)
    return { activeOnSelection, bars }
}

const NavigationLoading = () => (
    <div id="floater" class="bottom left">
        <Pulse />
    </div>
)

export function Navigation() {
    const emptySet = new Set<number>()
    const [selection, setSelection] = createSignal<number | null>(null)

    const [context] = createResource(async () => {
        const { activeOnSelection, bars } = processNavigationStructure(
            (await fetchPackageAsync(".ui/navigation")) as ScopeSchema
        )
        return {
            activeOnSelection,
            bars: bars.sort((a, b) => a.id - b.id),
        }
    })

    const active = createMemo(
        () => context()?.activeOnSelection.get(selection() ?? 0) ?? emptySet,
        emptySet
    )

    const select = (id: number | null) => {
        setSelection(id)
        document.getElementById("content")?.classList.add("backoff")
    }

    return (
        <Show when={context()} fallback={<NavigationLoading />}>
            <div
                id="floater"
                class="bottom left"
                on:mouseleave={() => {
                    select(null)
                    document
                        .getElementById("content")
                        ?.classList.remove("backoff")
                }}
            >
                <For each={context()?.bars}>
                    {bar => (
                        <Bar
                            {...bar}
                            selection={selection}
                            active={active}
                            select={select}
                        />
                    )}
                </For>
            </div>
        </Show>
    )
}

const Bar = (props: NavigationBar & NavigationState) => (
    <div
        classList={{
            menubar: true,
            current: props.selection() === props.id,
            active:
                props.active().has(props.id) || props.selection() === props.id,
        }}
    >
        <div class="menu">
            <For each={props.items}>
                {item =>
                    item.isScope ? (
                        <Scope
                            {...item}
                            selection={props.selection}
                            select={props.select}
                            active={props.active}
                        />
                    ) : (
                        <Item {...item} />
                    )
                }
            </For>
        </div>
    </div>
)

const Scope = (props: NavigationScope & NavigationState) => (
    <div
        on:click={() => props.select(props.id)}
        classList={{
            item: true,
            active:
                props.active().has(props.id) || props.selection() === props.id,
            current: props.selection() === props.id,
        }}
    >
        <DefaultIcon code={props.icon} /> {props.label}
        <AppIcon name={`chevron_right`} />
    </div>
)

const Item = (props: NavigationItem) => (
    <div
        draggable={true}
        on:dragstart={event => {
            event.dataTransfer!.setData("label", props.label)
            event.dataTransfer!.setData("link", props.url)
        }}
        class={`item grab`}
    >
        <DefaultIcon code={props.icon} /> {props.label}
    </div>
)
