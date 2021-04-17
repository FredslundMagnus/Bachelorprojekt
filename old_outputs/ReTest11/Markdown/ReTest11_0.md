
# Parameters

    Name :                      ReTest11-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67558035217 function calls (67305081774 primitive calls) in 86113.59 seconds

##    Ordered by: cumulative time
   List reduced from 504 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.585 86113.585 {built-in method builtins.exec}
                      1    4.221    4.221 86113.585 86113.585 <string>:1(<module>)
                      1  374.815  374.815 86109.364 86109.364 main.py:75(CFagent)
                9449256   46.258    0.000 29534.553    0.003 agent.py:29(learn)
                9445620  701.850    0.000 24165.133    0.003 learner.py:42(Qlearn)
                3149752   17.595    0.000 19994.051    0.006 game.py:41(step)
                3149752   21.072    0.000 19128.928    0.006 layers.py:718(step)
                3149752  301.260    0.000 13106.953    0.004 layers.py:17(step)
              312603626  929.843    0.000 12777.195    0.000 layer.py:98(move)
                3149752  127.175    0.000 11454.692    0.004 agent.py:54(_learn)
        284526602/31574850 1175.433    0.000 11402.901    0.000 module.py:715(_call_impl)
               22129230   55.702    0.000 10580.689    0.000 network.py:24(forward)
                3149752  123.019    0.000 10486.593    0.003 agent.py:202(_learn)
               22129230  306.731    0.000 10368.737    0.000 container.py:115(forward)
                9445620   70.299    0.000 9542.936    0.001 grad_mode.py:23(decorate_context)
                9445620  355.829    0.000 9345.057    0.001 adam.py:55(step)
                3149752 1157.527    0.000 8124.876    0.003 agent.py:210(counterfact)
              312603626 1477.638    0.000 7688.175    0.000 layers.py:735(check)
                9445620 1726.927    0.000 7658.182    0.001 functional.py:53(adam)
                3149752  102.819    0.000 7523.597    0.002 agent.py:117(_learn)
                3149752 4998.119    0.002 6512.592    0.002 replaybuffer.py:22(sample_data)
                3149753  477.170    0.000 5967.298    0.002 layers.py:684(update)
                3149752 4385.274    0.001 5858.990    0.002 replaybuffer.py:52(sample_data)
                9445620   62.905    0.000 5844.813    0.001 tensor.py:181(backward)
                9445620   42.030    0.000 5781.907    0.001 __init__.py:68(backward)
                9445620 5495.173    0.001 5495.173    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               50255600 5489.482    0.000 5489.482    0.000 {built-in method tensor}
               42990444   28.210    0.000 5269.953    0.000 game.py:37(board)
                6336322  192.091    0.000 5126.564    0.001 agent.py:49(__call__)
               62995050 2617.419    0.000 4561.736    0.000 layer.py:151(update)
                3149752 1833.660    0.001 4336.415    0.001 agent.py:88(interveen)
               44258460   78.926    0.000 3861.336    0.000 conv.py:422(forward)
               44258460  105.754    0.000 3745.492    0.000 conv.py:414(_conv_forward)
               44258460 3622.118    0.000 3622.118    0.000 {built-in method conv2d}
              312603626  651.437    0.000 3522.174    0.000 layers.py:729(isFree)
                3149752 1861.441    0.001 3380.340    0.001 replaybuffer.py:28(teleporter_save_data)
               60088186  132.948    0.000 3329.902    0.000 linear.py:92(forward)
                3149752 1585.143    0.001 3174.564    0.001 agent.py:67(modify)
               60088186  231.844    0.000 3122.526    0.000 functional.py:1669(linear)
             2950447122 2371.894    0.000 2870.738    0.000 layer.py:95(isFree)
               40965414 2614.481    0.000 2614.481    0.000 {built-in method cat}
              617096956 1424.817    0.000 2359.265    0.000 tensor.py:933(grad)
             1191466508  647.266    0.000 2234.162    0.000 {built-in method builtins.any}
               60088186 2207.045    0.000 2207.045    0.000 {built-in method addmm}
                9445620  195.567    0.000 2038.428    0.000 optimizer.py:167(zero_grad)
                3149752 1189.978    0.000 1791.002    0.001 replaybuffer.py:58(CF_save_data)
                3146116   59.788    0.000 1742.333    0.001 agent.py:171(__call__)
                9486074   75.909    0.000 1581.093    0.000 agent.py:59(modify_board)
                3149752   58.992    0.000 1562.997    0.000 agent.py:112(__call__)
              176313392 1551.342    0.000 1551.342    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              134143114 1536.395    0.000 1536.395    0.000 {built-in method clone}
             5808099956 1059.637    0.000 1512.074    0.000 enum.py:646(__hash__)
               82217416   80.818    0.000 1412.570    0.000 activation.py:713(forward)
               31599038  183.500    0.000 1343.526    0.000 tensor.py:21(wrapped)
               82217416  118.836    0.000 1331.752    0.000 functional.py:1292(leaky_relu)
              176313392 1264.158    0.000 1264.158    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              796940383  418.784    0.000 1264.100    0.000 overrides.py:1070(has_torch_function)
                3149752   64.449    0.000 1255.110    0.000 replaybuffer.py:18(stacker)
                3146116   59.405    0.000 1220.702    0.000 replaybuffer.py:48(stacker)
              312603626  924.539    0.000 1211.819    0.000 layers.py:77(check)
               82217416 1201.996    0.000 1201.996    0.000 {built-in method torch._C._nn.leaky_relu}
              978865748 1162.827    0.000 1162.827    0.000 layer.py:146(elements)
             3436366406  914.989    0.000 1105.566    0.000 layers.py:700(<genexpr>)
              312603626  711.546    0.000 1089.405    0.000 layers.py:246(check)
                9486074 1024.266    0.000 1024.266    0.000 {built-in method torch._C._nn.one_hot}
              312603626  619.960    0.000 1010.050    0.000 layers.py:286(check)
                2578354   33.534    0.000  998.252    0.000 layers.py:740(restart)
               88156696  886.221    0.000  886.221    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               88156696  838.532    0.000  838.532    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               88156696  722.429    0.000  722.429    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              312603626  567.434    0.000  712.158    0.000 layers.py:62(check)
                2578354   15.699    0.000  711.528    0.000 level.py:8(__init__)
             7717407716  708.475    0.000  708.475    0.000 layer.py:91(positions)
               88156696  641.841    0.000  641.841    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        7626076285/7626076282  485.164    0.000  603.128    0.000 {built-in method builtins.len}
                3149752  343.171    0.000  588.534    0.000 collector.py:46(collect)
                6336322  195.192    0.000  563.791    0.000 exploration.py:53(softmaxer)
              312603626  370.563    0.000  560.025    0.000 layers.py:273(check)
                2578354   94.181    0.000  555.004    0.000 levels.py:199(generate)
                9445620   17.950    0.000  552.080    0.000 loss.py:445(forward)
              346574338   95.629    0.000  546.659    0.000 {built-in method builtins.all}
               11456212  211.106    0.000  544.436    0.000 random.py:315(sample)
                9445620   66.134    0.000  534.130    0.000 functional.py:2637(mse_loss)
              312603626  324.668    0.000  517.496    0.000 layers.py:313(check)
                3149752   87.894    0.000  499.387    0.000 agent.py:277(counterfact_check)
                6297134  484.649    0.000  484.649    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             1685567357  380.352    0.000  474.508    0.000 overrides.py:1083(<genexpr>)
               88156696  469.825    0.000  469.825    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              822126442  205.944    0.000  466.385    0.000 layers.py:690(<genexpr>)
              312603626  323.134    0.000  463.733    0.000 layers.py:48(check)
              146775304  455.503    0.000  455.503    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             5808135827  452.444    0.000  452.444    0.000 {built-in method builtins.hash}
               22048264  442.643    0.000  442.643    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               60088186  412.667    0.000  412.667    0.000 {method 't' of 'torch._C._TensorBase' objects}
                5156708   44.660    0.000  373.890    0.000 level.py:41(notUsed)
              312603626  228.476    0.000  338.261    0.000 layers.py:23(check)
                9445620  306.994    0.000  306.994    0.000 {built-in method torch._C._nn.mse_loss}
              273022233  218.037    0.000  300.998    0.000 layer.py:126(remove)
             2330028260  284.671    0.000  284.671    0.000 layer.py:203(isBlocking)
                9446567  282.146    0.000  282.146    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9515002: <ReTest11_0> in cluster <dcc> Done

Job <ReTest11_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Apr 14 13:56:06 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 15 11:03:49 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 15 11:03:49 2021
Terminated at Fri Apr 16 10:59:08 2021
Results reported at Fri Apr 16 10:59:08 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85896.05 sec.
    Max Memory :                                 3310 MB
    Average Memory :                             3277.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13074.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            162182 sec.

The output (if any) is above this job summary.

