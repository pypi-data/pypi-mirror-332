# git-presets

The CLI tool to use multiple git config presets easily.

## Usage

### `set` and `use`

Making the `work` preset and use it

```sh
git-presets set work user.name a4rcvv
git-presets set work user.email "a4rcvv@example.tld"
git-presets use work

# git-presets runs these commands internally:
# git config user.name a4rcvv
# git config user.email "a4rcvv@example.tld"
```

### `show`

Show defined presets

```sh
git-presets show  # show all presets
git-presets show work # show the `work` preset
```

### `unset`

Unset an attribute from the preset

```sh
git-presets unset work user.name
```

### `remove`

Remove the `work` preset

```sh
git-presets remove work
```

### Show help

Use `-h` option to show more help.

```sh
git-presets -h
```