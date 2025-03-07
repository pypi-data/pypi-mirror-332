use pyo3::prelude::*;

#[cfg_attr(not(feature = "std"), no_std)]
// Hybrid SIMD width usage currently requires unstable 'stdsimd'
#[cfg_attr(feature = "hybrid", feature(stdarch_x86_avx512))]

#[rustfmt::skip]
mod gxhash;
pub use crate::gxhash::*;

#[cfg(feature = "std")]
mod hasher;
#[cfg(feature = "std")]
pub use crate::hasher::*;

#[pyfunction]
fn hash32(input: &[u8], seed: i64) -> PyResult<u32> {
    Ok(gxhash::gxhash32(input, seed))
}

#[pyfunction]
fn hash64(input: &[u8], seed: i64) -> PyResult<u64> {
    Ok(gxhash::gxhash64(input, seed))
}

#[pyfunction]
fn hash128(input: &[u8], seed: i64) -> PyResult<u128> {
    Ok(gxhash::gxhash128(input, seed))
}

#[pymodule]
fn gxhashpy(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hash32, m)?)?;
    m.add_function(wrap_pyfunction!(hash64, m)?)?;
    m.add_function(wrap_pyfunction!(hash128, m)?)?;
    Ok(())
}