import React from 'react';
import clsx from 'clsx';
import styles from './Highlights.module.css';
import Gradients from './Gradients';

const FeatureList = [
    {
        title: 'Python with type hints',
        Svg: require('../../static/img/features/runs-on-py.svg').default,
        description: (
            <>
                Crawlee for Python is written in a modern way using type hints, providing code completion in your IDE
                and helping you catch bugs early on build time.
            </>
        ),
    },
    // {
    //     title: 'HTTP scraping',
    //     Svg: require('../../static/img/features/fingerprints.svg').default,
    //     description: (
    //         <>
    //             Crawlee makes HTTP requests that <a href="https://crawlee.dev/docs/guides/avoid-blocking"><b>mimic browser headers and TLS fingerprints</b></a>.
    //             It also rotates them automatically based on data about real-world traffic. Popular HTML
    //             parsers <b><a href="https://crawlee.dev/docs/guides/cheerio-crawler-guide">Cheerio</a>&nbsp;
    //             and <a href="https://crawlee.dev/docs/guides/jsdom-crawler-guide">JSDOM</a></b> are included.
    //         </>
    //     ),
    // },
    {
        title: 'Headless browsers',
        Svg: require('../../static/img/features/works-everywhere.svg').default,
        description: (
            <>
                Switch your crawlers from HTTP to a <a href="https://crawlee.dev/python/api/class/PlaywrightCrawler">headless browser</a> in 3 lines of code.
                Crawlee builds on top of <b>Playwright</b> and adds its own features. Chrome, Firefox and more.
            </>
        ),

        // TODO: this is not true yet
        // Crawlee builds on top of <b>Playwright</b> and adds its own <b>anti-blocking features and human-like fingerprints</b>. Chrome, Firefox and more.
    },
    {
        title: 'Automatic scaling and proxy management',
        Svg: require('../../static/img/features/auto-scaling.svg').default,
        description: (
            <>
                Crawlee automatically manages concurrency based on <a href="https://crawlee.dev/python/api/class/AutoscaledPool">available system resources</a> and&nbsp;
                <a href="https://crawlee.dev/python/api/class/ProxyConfiguration">smartly rotates proxies</a>.
                Proxies that often time-out, return network errors or bad HTTP codes like 401 or 403 are discarded.
            </>
        ),
    },
    // {
    //     title: 'Queue and Storage',
    //     Svg: require('../../static/img/features/storage.svg').default,
    //     description: (
    //         <>
    //             You can <a href="https://crawlee.dev/docs/guides/result-storage">save files, screenshots and JSON results</a> to disk with one line of code
    //             or plug an adapter for your DB. Your URLs are <a href="https://crawlee.dev/docs/guides/request-storage">kept in a queue</a> that ensures their
    //             uniqueness and that you don't lose progress when something fails.
    //         </>
    //     ),
    // },
    // {
    //     title: 'Helpful utils and configurability',
    //     Svg: require('../../static/img/features/node-requests.svg').default,
    //     description: (
    //         <>
    //             Crawlee includes tools for <a href="https://crawlee.dev/api/utils/namespace/social">extracting social handles</a> or phone numbers, infinite scrolling, blocking
    //             unwanted assets <a href="https://crawlee.dev/api/utils">and many more</a>. It works great out of the box, but also provides&nbsp;
    //             <a href="https://crawlee.dev/api/basic-crawler/interface/BasicCrawlerOptions">rich configuration options</a>.
    //         </>
    //     ),
    // },
];

function Feature({ Svg, title, description }) {
    return (
        <div className={clsx('col col--4')}>
            <div className="padding-horiz--md padding-bottom--md">
                <div className={styles.featureIcon}>
                    {Svg ? <Svg alt={title}/> : null}
                </div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
    );
}

export default function Highlights() {
    return (
        <section className={styles.features}>
            <Gradients />
            <div className="container">
                <div className="row">
                    {FeatureList.map((props, idx) => (
                        <Feature key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>
    );
}
