use pyo3::prelude::*;
use sha2::{self, Digest};

/// Placeholder for store function which returns the blob_id.
#[pyfunction]
fn compute_sha256_digest(blob: &[u8]) -> PyResult<String> {
    // TODO: Implement store.
    Ok(hex::encode(sha2::Sha256::digest(blob)))
}

#[pymodule]
fn mystenlabs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(compute_sha256_digest))?;

    Ok(())
}
