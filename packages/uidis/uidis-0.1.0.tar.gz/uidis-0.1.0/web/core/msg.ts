export type Parser<T> = (input: unknown) => T

export type Def = Record<string, Parser<any>>

export type Schema<D extends Def> = {
    [K in keyof D]: D[K] extends (input: unknown) => infer T ? T : never
}

export type Struct<D extends Def> = {
    readonly parse: (input: unknown) => Schema<D>
    readonly tagged: (input: unknown) => Schema<D> & { tag: number }
}

export type Output<S extends Struct<any>> = S extends Struct<any>
    ? S extends {
          parse: (input: unknown) => infer T
          tagged: (input: unknown) => infer T & { tag: number }
      }
        ? T
        : never
    : never

export type TaggedOutput<S extends Struct<any>> = S extends Struct<any>
    ? S extends {
          parse: (input: unknown) => infer T
          tagged: (input: unknown) => infer T & { tag: number }
      }
        ? T & { tag: number }
        : never
    : never

export function def<T extends Record<string, Parser<any>>>(
    name: string,
    schema: T
) {
    const entries = Object.entries(schema)
    const lenEntries = entries.length * 1

    const parse = (input: unknown): Schema<T> => {
        if (!Array.isArray(input))
            throw new Error(
                `Invalid ${name}: expected array but got ${typeof input}`
            )
        try {
            if (input.length !== lenEntries)
                throw new Error(
                    `Invalid ${name} length: ${input.length} instead of ${lenEntries}`
                )

            return Object.fromEntries(
                entries.map(([key, validator], index) => [
                    key,
                    validator(input[index]),
                ])
            ) as Schema<T>
        } catch (error) {
            throw new Error(`Invalid ${name}`, { cause: error })
        }
    }

    const tagged = (input: unknown) => {
        if (!Array.isArray(input))
            throw new Error(
                `Invalid ${name}: expected array but got ${typeof input}`
            )

        const [tag, ...rest] = input
        if (typeof tag !== "number")
            throw new Error(
                `Invalid ${name} tag: expected number but got ${typeof tag}`
            )

        return { tag, ...parse(rest) }
    }

    return { parse, tagged } as const
}

export const string: Parser<string> = (input: unknown): string => {
    if (typeof input !== "string")
        throw new Error(`Expected string but got ${typeof input}`)
    return input
}

export const number: Parser<number> = (input: unknown): number => {
    if (typeof input !== "number")
        throw new Error(`Expected number but got ${typeof input}`)
    return input
}

export const url: Parser<string> = (input: unknown): string => {
    const str = string(input)
    try {
        new URL(str)
        return str
    } catch {
        throw new Error(`Invalid URL: ${str}`)
    }
}

export const enums =
    <T>(enums: readonly T[]) =>
    (input: unknown): T =>
        enums[number(input)]

export const nullable =
    <T>(parser: Parser<T>) =>
    (input: unknown): T | null =>
        input === null ? null : parser(input)

export const boolean: Parser<boolean> = (input: unknown): boolean => {
    if (typeof input !== "boolean")
        throw new Error(`Expected boolean but got ${typeof input}`)
    return input
}

export const array =
    <T>(parser: Parser<T>) =>
    (input: unknown): T[] => {
        if (!Array.isArray(input))
            throw new Error(`Expected array but got ${typeof input}`)
        return input.map(parser)
    }

export const transform =
    <T, U>(parser: Parser<T>, transform: (input: T) => U) =>
    (input: unknown): U =>
        transform(parser(input))

export const oneOf =
    <T, Ts extends T[]>(...parsers: { [K in keyof Ts]: Parser<Ts[K]> }) =>
    <T extends Ts[number]>(input: unknown): T => {
        for (const parser of parsers) {
            try {
                return parser(input) as unknown as T
            } catch {}
        }
        throw new Error(`None of the parsers matched`)
    }
