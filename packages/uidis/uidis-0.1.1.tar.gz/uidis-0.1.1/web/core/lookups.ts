import { validateCache } from "./cache"
import { fetchPackageAsync } from "./server"

const LookupMemory: Record<string, string> = {}

export async function lookup(name: string, code: number): Promise<string> {
    const key = `.ui/lookup/${name}/${code}`
    const memCache = LookupMemory[key]
    if (memCache !== undefined) return memCache

    await validateCache()
    const storageCache = localStorage.getItem(key)

    if (storageCache !== null) {
        LookupMemory[key] = storageCache
        return storageCache
    }

    const data = (await fetchPackageAsync(key)) as string
    localStorage.setItem(key, data)
    LookupMemory[key] = data
    return data
}

export const resolver = (name: string, code: number) => async () =>
    await lookup(name, code)
