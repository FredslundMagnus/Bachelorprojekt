
# Parameters

    Name :                      DoorsAndKey_teleport-2
    Main :                      teleport
    Level :                     Levels.Causal1
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      81751140975 function calls (81458080084 primitive calls) in 86104.83 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.832 86104.832 {built-in method builtins.exec}
                      1    1.530    1.530 86104.832 86104.832 <string>:1(<module>)
                      1  212.879  212.879 86103.302 86103.302 main.py:45(teleport)
               10467584   33.276    0.000 27614.497    0.003 agent.py:29(learn)
               10467584  663.057    0.000 23264.992    0.002 learner.py:42(Qlearn)
                5233792   19.069    0.000 21470.360    0.004 game.py:41(step)
                5233792   26.604    0.000 20452.816    0.004 layers.py:718(step)
                5233792  159.053    0.000 16676.939    0.003 agent.py:54(_learn)
                5233792 6858.625    0.001 12423.707    0.002 replaybuffer.py:28(teleporter_save_data)
        329693718/36633838 1148.177    0.000 11376.426    0.000 module.py:715(_call_impl)
                5233793  687.126    0.000 11110.914    0.002 layers.py:684(update)
                5233792  135.175    0.000 10886.245    0.002 agent.py:117(_learn)
               26166254   59.037    0.000 10611.233    0.000 network.py:27(forward)
               26166254  279.578    0.000 10412.183    0.000 container.py:115(forward)
                5233792 6239.185    0.001 9729.796    0.002 agent.py:88(interveen)
               10467584   59.698    0.000 9362.019    0.001 grad_mode.py:23(decorate_context)
                5233792  400.380    0.000 9278.798    0.002 layers.py:17(step)
               10467584  306.900    0.000 9193.935    0.001 adam.py:55(step)
              523379200  794.360    0.000 8833.321    0.000 layer.py:98(move)
               10467584 1693.509    0.000 7551.949    0.001 functional.py:53(adam)
               10464878  209.457    0.000 7046.326    0.001 agent.py:49(__call__)
                5233792 3977.073    0.001 6173.302    0.001 replaybuffer.py:22(sample_data)
               10467584   54.086    0.000 5459.074    0.001 tensor.py:181(backward)
               10467584   35.838    0.000 5404.989    0.001 __init__.py:68(backward)
               16247328  118.909    0.000 5306.073    0.000 layers.py:740(restart)
               10467584 5146.175    0.000 5146.175    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5233792 2664.987    0.001 4871.552    0.001 agent.py:67(modify)
              450838674 4401.820    0.000 4401.820    0.000 {built-in method clone}
              523379200 1275.850    0.000 4351.457    0.000 layers.py:735(check)
               16247328   59.262    0.000 4110.164    0.000 level.py:8(__init__)
               52332508   81.525    0.000 3877.227    0.000 conv.py:422(forward)
               52332508   92.687    0.000 3764.186    0.000 conv.py:414(_conv_forward)
               52332508 3654.332    0.000 3654.332    0.000 {built-in method conv2d}
               16247328  172.862    0.000 3472.216    0.000 levels.py:122(generate)
               68031178  136.522    0.000 3349.378    0.000 linear.py:92(forward)
               68031178  235.917    0.000 3149.748    0.000 functional.py:1669(linear)
               63364185  547.114    0.000 3142.526    0.000 level.py:41(notUsed)
              523379200  676.502    0.000 2896.234    0.000 layers.py:729(isFree)
              659457846 1443.963    0.000 2382.170    0.000 tensor.py:933(grad)
               31402758 1402.725    0.000 2329.646    0.000 layer.py:167(NoRock_update)
             1454433703  690.001    0.000 2248.197    0.000 {built-in method builtins.any}
               68031178 2229.905    0.000 2229.905    0.000 {built-in method addmm}
                5233792   65.324    0.000 2221.365    0.000 agent.py:112(__call__)
             3047330067 1782.190    0.000 2219.731    0.000 layer.py:95(isFree)
               41867630 2207.581    0.000 2207.581    0.000 {built-in method cat}
               15698670   98.494    0.000 2164.189    0.000 agent.py:59(modify_board)
               10467584  188.602    0.000 2058.560    0.000 optimizer.py:167(zero_grad)
                5233792   79.747    0.000 1837.163    0.000 replaybuffer.py:18(stacker)
             6322687094 1053.571    0.000 1533.595    0.000 enum.py:646(__hash__)
              188416512 1512.935    0.000 1512.935    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94197432   71.644    0.000 1435.808    0.000 activation.py:713(forward)
               63364185   45.410    0.000 1426.196    0.000 level.py:38(elementsIn)
               15698670 1398.273    0.000 1398.273    0.000 {built-in method torch._C._nn.one_hot}
               22319971 1393.662    0.000 1393.662    0.000 {built-in method tensor}
               94197432  107.741    0.000 1364.164    0.000 functional.py:1292(leaky_relu)
              858335384  424.714    0.000 1281.325    0.000 overrides.py:1070(has_torch_function)
              188416512 1269.314    0.000 1269.314    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              466537344 1252.516    0.000 1252.516    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               94197432 1245.378    0.000 1245.378    0.000 {built-in method torch._C._nn.leaky_relu}
               36639060  177.563    0.000 1218.081    0.000 tensor.py:21(wrapped)
              560018360  124.576    0.000 1195.814    0.000 {built-in method builtins.all}
             1130910963  238.498    0.000 1109.093    0.000 layers.py:690(<genexpr>)
             3549923804  867.723    0.000 1079.329    0.000 layers.py:700(<genexpr>)
               10467584   10.977    0.000 1069.920    0.000 game.py:37(board)
               97483968   86.823    0.000 1043.718    0.000 layer.py:69(restart)
               63364185  453.496    0.000  917.025    0.000 level.py:39(<listcomp>)
              523379200  565.101    0.000  890.091    0.000 layers.py:141(check)
               94208256  882.205    0.000  882.205    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5233792  507.593    0.000  877.445    0.000 collector.py:46(collect)
              523379300  566.543    0.000  856.345    0.000 layers.py:113(isDone)
               94208256  807.627    0.000  807.627    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               16247428  394.876    0.000  794.115    0.000 layers.py:36(reset)
               10464878  271.028    0.000  733.559    0.000 exploration.py:53(softmaxer)
             2922813438  731.218    0.000  731.218    0.000 level.py:32(inverse)
               94208256  725.865    0.000  725.865    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              523379200  453.070    0.000  696.378    0.000 layers.py:48(check)
              523379200  413.328    0.000  643.048    0.000 layers.py:124(check)
               94208256  636.767    0.000  636.767    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6965468133  619.621    0.000  619.621    0.000 layer.py:91(positions)
             1133775270  424.737    0.000  591.990    0.000 layer.py:130(add)
             2314528619  588.853    0.000  588.853    0.000 layer.py:146(elements)
               16247328  295.192    0.000  544.953    0.000 level.py:16(<dictcomp>)
              523379200  356.677    0.000  522.102    0.000 layers.py:23(check)
             2866015922  506.455    0.000  506.455    0.000 enum.py:352(<genexpr>)
               10467584   15.909    0.000  494.033    0.000 loss.py:445(forward)
        5050392305/5050392303  354.869    0.000  487.912    0.000 {built-in method builtins.len}
               94208256  484.305    0.000  484.305    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6322725149  480.031    0.000  480.031    0.000 {built-in method builtins.hash}
               10467584   55.634    0.000  478.124    0.000 functional.py:2637(mse_loss)
             1821339960  381.119    0.000  472.260    0.000 overrides.py:1083(<genexpr>)
               63364185  287.681    0.000  463.761    0.000 {built-in method _functools.reduce}
               26168960  452.571    0.000  452.571    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               68031178  398.235    0.000  398.235    0.000 {method 't' of 'torch._C._TensorBase' objects}
              524873539  242.680    0.000  363.952    0.000 layer.py:126(remove)
               31402752  359.676    0.000  359.676    0.000 {built-in method sum}
                5233792  127.164    0.000  350.225    0.000 random.py:315(sample)
                5235884  331.953    0.000  331.953    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             3757089951  289.172    0.000  289.172    0.000 {method 'random' of '_random.Random' objects}
               10467584  279.253    0.000  279.253    0.000 {built-in method torch._C._nn.mse_loss}
             3390092608  268.946    0.000  268.946    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550928: <DoorsAndKey_teleport_2> in cluster <dcc> Done

Job <DoorsAndKey_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:53 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 27 08:58:06 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 08:58:06 2021
Terminated at Wed Apr 28 08:53:15 2021
Results reported at Wed Apr 28 08:53:15 2021

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

    CPU time :                                   85899.09 sec.
    Max Memory :                                 2681 MB
    Average Memory :                             2678.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13703.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86109 sec.
    Turnaround time :                            664282 sec.

The output (if any) is above this job summary.

