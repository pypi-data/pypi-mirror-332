# Changelog

## 0.5.0 (2025-03-08)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** update via SDK Studio ([58760a2](https://github.com/aigc-libs/pyopenwebui-python/commit/58760a2500244b8c5624f7eb86794f693615f2b2))
* **api:** update via SDK Studio ([cb90dff](https://github.com/aigc-libs/pyopenwebui-python/commit/cb90dff53133f9c8ddbf25e57be7186d8f750286))
* **api:** update via SDK Studio ([0ea42bf](https://github.com/aigc-libs/pyopenwebui-python/commit/0ea42bfbb01913663e50d9e5f965a3d8e3d1f801))
* **api:** update via SDK Studio ([12d3f3f](https://github.com/aigc-libs/pyopenwebui-python/commit/12d3f3f1ce6f508e9725656f632f29287a806d0b))
* **api:** update via SDK Studio ([#50](https://github.com/aigc-libs/pyopenwebui-python/issues/50)) ([a20862b](https://github.com/aigc-libs/pyopenwebui-python/commit/a20862b2fd41587723b15acb2e7a1510edfbac04))

## 0.4.0 (2025-03-08)

Full Changelog: [v0.3.22...v0.4.0](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.3.22...v0.4.0)

### Features

* **api:** update via SDK Studio ([#46](https://github.com/aigc-libs/pyopenwebui-python/issues/46)) ([b3a6c2e](https://github.com/aigc-libs/pyopenwebui-python/commit/b3a6c2e23c79114420a268a05470ef12e416830e))
* **api:** update via SDK Studio ([#48](https://github.com/aigc-libs/pyopenwebui-python/issues/48)) ([efb974b](https://github.com/aigc-libs/pyopenwebui-python/commit/efb974b1599eb4bb707086024a36b95d07dadeee))

## 0.3.22 (2025-01-25)

Full Changelog: [v0.3.21...v0.3.22](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.3.21...v0.3.22)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#18](https://github.com/aigc-libs/pyopenwebui-python/issues/18)) ([049072f](https://github.com/aigc-libs/pyopenwebui-python/commit/049072f0ff756f9ea31d7e1a2a4c99b250ef709c))
* **client:** only call .close() when needed ([#34](https://github.com/aigc-libs/pyopenwebui-python/issues/34)) ([36403bb](https://github.com/aigc-libs/pyopenwebui-python/commit/36403bbf0f35f45084cd54cbaa3a046dbce2d0bc))
* correctly handle deserialising `cls` fields ([#36](https://github.com/aigc-libs/pyopenwebui-python/issues/36)) ([db9fac4](https://github.com/aigc-libs/pyopenwebui-python/commit/db9fac4d450d3a6d14aa11cafe91d0000f6e63c6))
* **tests:** make test_get_platform less flaky ([#40](https://github.com/aigc-libs/pyopenwebui-python/issues/40)) ([4d76b93](https://github.com/aigc-libs/pyopenwebui-python/commit/4d76b9310ad0743a0d320d7bfc9e18610061a6ce))


### Chores

* **internal:** add support for TypeAliasType ([#24](https://github.com/aigc-libs/pyopenwebui-python/issues/24)) ([dd417b3](https://github.com/aigc-libs/pyopenwebui-python/commit/dd417b38a27a56cf42960e0eae4a9352d837401b))
* **internal:** avoid pytest-asyncio deprecation warning ([#41](https://github.com/aigc-libs/pyopenwebui-python/issues/41)) ([68e90fa](https://github.com/aigc-libs/pyopenwebui-python/commit/68e90faa5333a06200e7d896c58e52cda59eb8e2))
* **internal:** bump httpx dependency ([#33](https://github.com/aigc-libs/pyopenwebui-python/issues/33)) ([ed64e14](https://github.com/aigc-libs/pyopenwebui-python/commit/ed64e14274fd26c1485b89993f35b3d04f4041e7))
* **internal:** bump pydantic dependency ([#21](https://github.com/aigc-libs/pyopenwebui-python/issues/21)) ([626883a](https://github.com/aigc-libs/pyopenwebui-python/commit/626883ab49a2b396a7e22492d4b45d34dd10edda))
* **internal:** bump pyright ([#23](https://github.com/aigc-libs/pyopenwebui-python/issues/23)) ([1f4e567](https://github.com/aigc-libs/pyopenwebui-python/commit/1f4e5671b846ab127ed688da50597bc4a109a5dd))
* **internal:** codegen related update ([#19](https://github.com/aigc-libs/pyopenwebui-python/issues/19)) ([2072439](https://github.com/aigc-libs/pyopenwebui-python/commit/20724395c7dd2aa1f8f717504177da606e709717))
* **internal:** codegen related update ([#25](https://github.com/aigc-libs/pyopenwebui-python/issues/25)) ([f9aca77](https://github.com/aigc-libs/pyopenwebui-python/commit/f9aca77705f5443b7375a63682d8457eab9470e7))
* **internal:** codegen related update ([#26](https://github.com/aigc-libs/pyopenwebui-python/issues/26)) ([f46b1f0](https://github.com/aigc-libs/pyopenwebui-python/commit/f46b1f0c84f32777472f9649c2639a785a246820))
* **internal:** codegen related update ([#31](https://github.com/aigc-libs/pyopenwebui-python/issues/31)) ([fce3014](https://github.com/aigc-libs/pyopenwebui-python/commit/fce30141e81edc964eec32142407eddd16bb5889))
* **internal:** codegen related update ([#32](https://github.com/aigc-libs/pyopenwebui-python/issues/32)) ([47cd339](https://github.com/aigc-libs/pyopenwebui-python/commit/47cd3392e58d5d0d34eab781a0af558e9a0ed897))
* **internal:** codegen related update ([#35](https://github.com/aigc-libs/pyopenwebui-python/issues/35)) ([b3eee85](https://github.com/aigc-libs/pyopenwebui-python/commit/b3eee854a71566bb6ae8f690023a50386f69eae1))
* **internal:** codegen related update ([#37](https://github.com/aigc-libs/pyopenwebui-python/issues/37)) ([8c77819](https://github.com/aigc-libs/pyopenwebui-python/commit/8c778197cfacd70391b778652b03109da2388cc5))
* **internal:** codegen related update ([#38](https://github.com/aigc-libs/pyopenwebui-python/issues/38)) ([8ce52a1](https://github.com/aigc-libs/pyopenwebui-python/commit/8ce52a1d756fced14ae17a46c1b2369bd8d37f0c))
* **internal:** codegen related update ([#42](https://github.com/aigc-libs/pyopenwebui-python/issues/42)) ([8cbaa73](https://github.com/aigc-libs/pyopenwebui-python/commit/8cbaa7397935b98eeedf41c0784be5bb44ded55f))
* **internal:** codegen related update ([#43](https://github.com/aigc-libs/pyopenwebui-python/issues/43)) ([986e14e](https://github.com/aigc-libs/pyopenwebui-python/commit/986e14ef258f43757b589168c784498d59888f37))
* **internal:** exclude mypy from running on tests ([#17](https://github.com/aigc-libs/pyopenwebui-python/issues/17)) ([2609c58](https://github.com/aigc-libs/pyopenwebui-python/commit/2609c582be9c465b12397fd383ad95ff5f3daefb))
* **internal:** fix compat model_dump method when warnings are passed ([#13](https://github.com/aigc-libs/pyopenwebui-python/issues/13)) ([3f58707](https://github.com/aigc-libs/pyopenwebui-python/commit/3f5870789a7e966e0ea1d183ff1b2c2743fa7c05))
* **internal:** fix some typos ([#30](https://github.com/aigc-libs/pyopenwebui-python/issues/30)) ([a4a7087](https://github.com/aigc-libs/pyopenwebui-python/commit/a4a70879341f0fcd53db39e03a42e98cee7143d3))
* **internal:** remove some duplicated imports ([#27](https://github.com/aigc-libs/pyopenwebui-python/issues/27)) ([2b9d923](https://github.com/aigc-libs/pyopenwebui-python/commit/2b9d923ec0db4d3e262289a9160ca527547d8594))
* **internal:** updated imports ([#28](https://github.com/aigc-libs/pyopenwebui-python/issues/28)) ([2a5e4fe](https://github.com/aigc-libs/pyopenwebui-python/commit/2a5e4fed5cf03552df2667a3f47105db184e0a27))
* make the `Omit` type public ([#20](https://github.com/aigc-libs/pyopenwebui-python/issues/20)) ([a699cbe](https://github.com/aigc-libs/pyopenwebui-python/commit/a699cbedd59f464afa6395792cd1d26975aee419))
* rebuild project due to codegen change ([#10](https://github.com/aigc-libs/pyopenwebui-python/issues/10)) ([c25250e](https://github.com/aigc-libs/pyopenwebui-python/commit/c25250ec15e6d900e5def60446a9516711d06927))
* rebuild project due to codegen change ([#11](https://github.com/aigc-libs/pyopenwebui-python/issues/11)) ([4d0620f](https://github.com/aigc-libs/pyopenwebui-python/commit/4d0620f84f23c3bcf8e278d3a1f6a50e777416c5))
* rebuild project due to codegen change ([#12](https://github.com/aigc-libs/pyopenwebui-python/issues/12)) ([8382297](https://github.com/aigc-libs/pyopenwebui-python/commit/8382297cb61011baac8d7841f2debf0a081dcf77))
* rebuild project due to codegen change ([#6](https://github.com/aigc-libs/pyopenwebui-python/issues/6)) ([50ba84d](https://github.com/aigc-libs/pyopenwebui-python/commit/50ba84d5f7ef2bb2fd62cb99ad4d02029466a4fb))
* rebuild project due to codegen change ([#8](https://github.com/aigc-libs/pyopenwebui-python/issues/8)) ([ebd0220](https://github.com/aigc-libs/pyopenwebui-python/commit/ebd02208b387ea4422fb834d16a536e95094daa0))
* rebuild project due to codegen change ([#9](https://github.com/aigc-libs/pyopenwebui-python/issues/9)) ([e064261](https://github.com/aigc-libs/pyopenwebui-python/commit/e064261a1186e0f891beebebc265181283232734))
* remove now unused `cached-property` dep ([#15](https://github.com/aigc-libs/pyopenwebui-python/issues/15)) ([8f2d4c9](https://github.com/aigc-libs/pyopenwebui-python/commit/8f2d4c99c0dbb012b756626b325bcdada61f0af6))


### Documentation

* add info log level to readme ([#14](https://github.com/aigc-libs/pyopenwebui-python/issues/14)) ([07724ce](https://github.com/aigc-libs/pyopenwebui-python/commit/07724ce9525b1e9aca4e6c68f49f7519bd830c45))
* **api.md:** fix return type annotations ([#16](https://github.com/aigc-libs/pyopenwebui-python/issues/16)) ([37df760](https://github.com/aigc-libs/pyopenwebui-python/commit/37df760b27db8a051a29c9c2b840915507c56a19))
* **raw responses:** fix duplicate `the` ([#39](https://github.com/aigc-libs/pyopenwebui-python/issues/39)) ([8dfcb08](https://github.com/aigc-libs/pyopenwebui-python/commit/8dfcb08bb3c9e00738d0664de4eeff787ec0949f))
* **readme:** example snippet for client context manager ([#29](https://github.com/aigc-libs/pyopenwebui-python/issues/29)) ([3ac892d](https://github.com/aigc-libs/pyopenwebui-python/commit/3ac892def0bcf77b3d3aafba19d98755c078bc44))
* **readme:** fix http client proxies example ([#22](https://github.com/aigc-libs/pyopenwebui-python/issues/22)) ([534ea9d](https://github.com/aigc-libs/pyopenwebui-python/commit/534ea9d0e0caf8b68a644a81a14c17808dc6acf2))

## 0.3.21 (2024-09-15)

Full Changelog: [v0.0.1-alpha.0...v0.3.21](https://github.com/aigc-libs/pyopenwebui-python/compare/v0.0.1-alpha.0...v0.3.21)

### Chores

* go live ([#1](https://github.com/aigc-libs/pyopenwebui-python/issues/1)) ([92afbcb](https://github.com/aigc-libs/pyopenwebui-python/commit/92afbcb7df1185b7999d4f8577ed85c1911f9e88))
* update SDK settings ([#3](https://github.com/aigc-libs/pyopenwebui-python/issues/3)) ([e8c18d1](https://github.com/aigc-libs/pyopenwebui-python/commit/e8c18d1be937313807521e95759bbab3fefac518))
