import { useLazyQuery } from '@apollo/client/react';
import { PRODUCTS_QUERY } from '../graphql/products_query';
import { useEffect, useState } from 'react';
import { pdf } from '@react-pdf/renderer';
import { ReportTemplate } from '../components/ReportTemplate';
import type { ProductListData } from '../graphql/productreport_query';

export default function ProductReport() {
  const [message, setMessage] = useState<string>('');
  const [productsQuery] = useLazyQuery<ProductListData>(PRODUCTS_QUERY);
  const [pdfUrl, setPdfUrl] = useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;

    const generateReport = async () => {
      setMessage('Loading Data & Generating PDF...');
      try {
        const { data } = await productsQuery();

        if (isMounted && data?.products?.reports) {
          const products = data.products.reports;
          const doc = <ReportTemplate products={products} />;
          
          // Generate Blob
          const blob = await pdf(doc).toBlob();
          const url = URL.createObjectURL(blob);

          if (isMounted) {
            setPdfUrl(url);
            setMessage('');
          } else {
            URL.revokeObjectURL(url); // Clean up if user left already
          }
        }
      } catch (err: any) {
        if (isMounted) {
          setMessage('Error loading report');
          console.error(err);
        }
      }
    };

    generateReport();

    return () => {
      isMounted = false;
      if (pdfUrl) URL.revokeObjectURL(pdfUrl);
    };
  }, []);

  return (
    <div className='container-fluid bg-dark vh-100 d-flex flex-column'>
      <div className='flex-grow-1 bg-white m-3 rounded overflow-hidden'>
        {message ? (
          <div className="d-flex text-dark justify-content-center align-items-center h-100">
            {message}
          </div>
        ) : (
          pdfUrl && <iframe key={pdfUrl} src={`${pdfUrl}#toolbar=1`} width="100%" height="100%" />
        )}
      </div>
    </div>
  );
}
