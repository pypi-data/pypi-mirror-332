{ nixpkgs, pynix, python_pkgs }:
let
  commit = "79e8c471fce0a0ebe40e1bfdf0bc4350d494eee1"; # v2.2.1
  sha256 = "0yyxnnyrdh26d1l69s3hf6107m6bc731kb7gvw5hjqb374x2wdca";
  bundle = let
    src = builtins.fetchTarball {
      inherit sha256;
      url =
        "https://gitlab.com/dmurciaatfluid/purity/-/archive/${commit}/purity-${commit}.tar";
    };
  in import "${src}/build" {
    inherit src;
    inherit nixpkgs pynix;
  };
  extended_python_pkgs = python_pkgs // {
    inherit (bundle.deps) types-simplejson;
  };
in bundle.builders.pkgBuilder
(bundle.builders.requirements extended_python_pkgs)
