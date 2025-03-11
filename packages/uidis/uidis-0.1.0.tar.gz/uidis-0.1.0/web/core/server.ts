import { decodeAsync } from "@msgpack/msgpack"

export type VersionType = [major: number, minor: number, patch: number]

var version: VersionType | null = null
var versionPromise: Promise<VersionType> | null = null

export const root =
    document
        .querySelector('meta[name="uidis"]')
        ?.attributes.getNamedItem("root")?.value ?? "/"

export async function fetchPackageAsync(
    path: string,
    options?: RequestInit
): Promise<unknown> {
    // simulate delay
    // await new Promise(resolve => setTimeout(resolve, 10000))
    const response = await fetch(root + path, options)
    const contentType = response.headers.get("Content-Type")
    if (contentType === "uidis" && response.body != null)
        return await decodeAsync(response.body)
    throw new Error("Invalid content type")
}

export async function getVersion(): Promise<VersionType> {
    if (version !== null) return version
    if (versionPromise !== null) return versionPromise
    versionPromise = fetchPackageAsync(".ui/version") as Promise<VersionType>

    try {
        version = await versionPromise
        return version
    } catch (error) {
        versionPromise = null
        throw error
    }
}
