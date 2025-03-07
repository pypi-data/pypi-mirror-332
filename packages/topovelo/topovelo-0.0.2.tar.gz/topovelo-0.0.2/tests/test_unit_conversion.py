import pytest
import numpy as np
import scanpy as sc

@pytest.fixture(scope='module')
def test_cases():
    return [
        ('/nfs/turbo/umms-welchjd/jialin/cytosignal_proj/slide-seq/adult_cortex/slide-seq-adult-cortex.h5ad'),
        
    ]