# NumPy mask-shift evaluation fixture

This small Python project isolates the scalar shift behavior described in
[isce3 issue #335](https://github.com/isce-framework/isce3/issues/335). It is
an independent, public evaluation input for ReproDelta. It does **not** import
or test isce3 or claim the full InSAR product is affected by this fixture.

The approved adapter is `mask_probe.measure`. Its JSON input is two integers,
`reference` and `secondary`, each in `0..255`. The numeric output is
`packed_mask`; the evaluation decision is whether `packed_mask > 65535`.
`{"reference": 3, "secondary": 1}` is the fixed sample. The same source
commit must run in environments prepared with NumPy `1.26.4` and `2.0.2`.

The pull request changes only the exact NumPy pin in `requirements.txt`, so a
paired result can be attributed to that controlled dependency change within
this narrow expression. A zero-mask input is an unchanged control. The
source-level `int()` cast reported in the issue can be tested separately as a
candidate repair; it is not part of the upgrade pull request.

To inspect the expression locally:

```sh
python -c "from mask_probe import measure; print(measure({'reference': 3, 'secondary': 1}))"
```
