{
  description = "A Python wrapper for the SSHBind Rust library";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

    crane.url = "github:ipetkov/crane";

    fenix = {
      url = "github:nix-community/fenix";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.rust-analyzer-src.follows = "";
    };

    flake-utils.url = "github:numtide/flake-utils";

    advisory-db = {
      url = "github:rustsec/advisory-db";
      flake = false;
    };

    statix.url = "github:oppiliappan/statix";
  };

  outputs = {
    self,
    nixpkgs,
    crane,
    fenix,
    flake-utils,
    advisory-db,
    statix,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system}.extend statix.overlays.default;

      inherit (pkgs) lib;

      craneLib =
        (crane.mkLib pkgs).overrideToolchain
        fenix.packages.${system}.stable.toolchain;

      src = craneLib.cleanCargoSource ./.;

      # Common arguments can be set here to avoid repeating them later
      commonArgs = {
        inherit src;
        strictDeps = true;

        buildInputs =
          [
            # Add additional build inputs here
            pkgs.maturin
            pkgs.openssl
          ]
          ++ lib.optionals pkgs.stdenv.isDarwin [
            # Additional darwin specific inputs can be set here
            pkgs.libiconv
          ];

        nativeBuildInputs = with pkgs; [sops libiconv pkg-config python3 perl];
        # Additional environment variables can be set directly
        LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [pkgs.openssl];
      };

      # Build *just* the cargo dependencies, so we can reuse
      # all of that work (e.g. via cachix) when running in CI
      cargoArtifacts = craneLib.buildDepsOnly commonArgs;

      # Build the actual crate itself, reusing the dependency
      # artifacts from above.
      sshbind-wrapper-python = craneLib.buildPackage (commonArgs
        // {
          inherit cargoArtifacts;
          doCheck = false;
        });

      # Build the python package from the crate
      sshbind = pkgs.python3Packages.callPackage ./sshbind.nix {};
    in {
      checks = {
        # Build the crate as part of `nix flake check` for convenience
        inherit sshbind-wrapper-python;

        # Run clippy (and deny all warnings) on the crate source,
        # again, reusing the dependency artifacts from above.
        #
        # Note that this is done as a separate derivation so that
        # we can block the CI if there are issues here, but not
        # prevent downstream consumers from building our crate by itself.
        sshbind-clippy = craneLib.cargoClippy (commonArgs
          // {
            inherit cargoArtifacts;
            cargoClippyExtraArgs = "--all-targets -- --deny warnings";
          });

        sshbind-doc = craneLib.cargoDoc (commonArgs
          // {
            inherit cargoArtifacts;
          });

        # Check formatting
        sshbind-fmt = craneLib.cargoFmt {
          inherit src;
        };

        sshbind-toml-fmt = craneLib.taploFmt {
          src = pkgs.lib.sources.sourceFilesBySuffices src [".toml"];
          # taplo arguments can be further customized below as needed
          # taploExtraArgs = "--config ./taplo.toml";
        };

        # Audit dependencies
        sshbind-audit = craneLib.cargoAudit {
          inherit src advisory-db;
        };

        # Audit licenses
        sshbind-deny = craneLib.cargoDeny {
          inherit src;
        };

        # Compilation and importing should be enough testing for this package
        # Run tests with cargo-nextest
        # Consider setting `doCheck = false` on `my-crate` if you do not want
        # the tests to run twice
        # sshbind-nextest = craneLib.cargoNextest (commonArgs
        #   // {
        #     inherit cargoArtifacts;
        #     partitions = 1;
        #     partitionType = "count";
        #     withLlvmCov = true;
        #   });
      };

      packages = {
        default = sshbind;
        rust-sshbind-wrapper = sshbind-wrapper-python;
      };

      apps.default = flake-utils.lib.mkApp {
        drv = sshbind;
      };

      formatter = pkgs.alejandra;

      devShells.default = craneLib.devShell {
        # Inherit inputs from checks.
        checks = self.checks.${system};

        LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [pkgs.openssl];
        # Additional dev-shell environment variables can be set directly
        # MY_CUSTOM_DEVELOPMENT_VAR = "something else";

        # Extra inputs can be added here; cargo and rustc are provided by default.
        packages = [
          self.packages.${system}.default
          pkgs.python3
          (pkgs.poetry.override {python3 = pkgs.python3;})
          pkgs.openssl
          pkgs.sops
          pkgs.pre-commit-hook-ensure-sops
          pkgs.age
          pkgs.statix
          pkgs.maturin
	  pkgs.perl
          # pkgs.ripgrep
        ];
      };
    });
}
