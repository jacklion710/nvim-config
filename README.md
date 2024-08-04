# My Neovim Configuration

Just keeping track of my nvim config with github. That way I can synchronize changes across many different machines.

## Introduction

I followed [The Primeagens](https://www.youtube.com/@ThePrimeagen) tutorial for setting up this configuration, however I decided to modify it to include a few extra things that are particular to my work such as LSP for python. As time goes on and I continue to learn more about neovim and lua it will likely diverge from Primes approach towards being better fitted for my work. He never mentions it in his video but I'm pretty sure you need to be using nvim version 0.8 or greater. See nvim documentation for instructions on installing the latest version.

## Features

- Modern and efficient text editing experience
- Customized key mappings for improved workflow
- Language Server Protocol (LSP) integration, including Python support
- Fuzzy finding capabilities with Telescope
- Git integration with Fugitive
- And more!

## Installation

1. Backup your existing Neovim configuration if you have one.
2. Clone this repository: `git clone https://github.com/yourusername/nvim-config.git ~/.config/nvim`
3. Install [Packer](https://github.com/wbthomason/packer.nvim) (plugin manager)
4. Open Neovim and run `:PackerSync` to install the plugins

## Key Mappings

Most of the key mappings follow The Primeagen's setup. For a comprehensive list, please refer to the files in `nvim/lua/jake/`. Some notable mappings include:

- `<leader>pv`: Open file explorer
- `<leader>ff`: Find files with Telescope
- `<C-p>`: Git files with Telescope

(I will document more key mappings soon)

## Plugins

This configuration uses the following plugins:

- [Rose Pine](https://github.com/rose-pine/neovim): A soothing color scheme
- [Fugitive](https://github.com/tpope/vim-fugitive): Git integration
- [Harpoon](https://github.com/ThePrimeagen/harpoon): Quick file navigation
- [LSP-Zero](https://github.com/VonHeikemen/lsp-zero.nvim): Easy LSP setup
- [Telescope](https://github.com/nvim-telescope/telescope.nvim): Fuzzy finder
- [Treesitter](https://github.com/nvim-treesitter/nvim-treesitter): Syntax highlighting and code navigation
- [Undotree](https://github.com/mbbill/undotree): Visualize undo history

## Customization

The main configuration files are located in `nvim/lua/jake/`. Feel free to explore and modify these files to suit your needs.

## Contributing

While this is primarily a personal configuration, suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## Acknowledgements

Special thanks to [The Primeagen](https://www.youtube.com/@ThePrimeagen) for the initial setup tutorial and inspiration. I'm actually really loving nvim, it reminds me of playing a really old terminal game yet its so powerful!

## License

This project is open source and available under the [MIT License](LICENSE).
