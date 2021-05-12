
# Parameters

    Name :                      Attempt6_Diamonds3_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal6
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      21286833007 function calls (20612374450 primitive calls) in 258900.66 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.662 258900.662 {built-in method builtins.exec}
                      1    0.295    0.295 258900.662 258900.662 <string>:1(<module>)
                      1 2283.877 2283.877 258900.367 258900.367 optionCritic.py:195(option_critic_run)
                 756119    5.578    0.000 183220.139    0.242 tensor.py:195(backward)
                 756119    6.602    0.000 183214.460    0.242 __init__.py:68(backward)
                 756119 183192.717    0.242 183192.717    0.242 {method 'run_backward' of 'torch._C._EngineBase' objects}
        892570573/220569823 4153.183    0.000 47842.515    0.000 module.py:866(_call_impl)
               24195808 3450.237    0.000 46476.897    0.002 optionCritic.py:143(actor_loss_fn)
               74666750  339.420    0.000 44665.527    0.001 optionCritic.py:70(get_state)
               74666750  942.831    0.000 43301.107    0.001 container.py:117(forward)
              149333500  403.034    0.000 27538.184    0.000 conv.py:398(forward)
              149333500  211.689    0.000 26979.004    0.000 conv.py:390(_conv_forward)
              149333500 26767.315    0.000 26767.315    0.000 {built-in method conv2d}
              295236573  704.964    0.000 9341.626    0.000 linear.py:93(forward)
              295236573  274.739    0.000 8356.077    0.000 functional.py:1737(linear)
               24195808 1367.004    0.000 8169.816    0.000 optionCritic.py:91(get_action)
              295236573 8018.656    0.000 8018.656    0.000 {built-in method torch._C._nn.linear}
               24195808  484.353    0.000 5641.477    0.000 optionCritic.py:80(predict_option_termination)
                 756119   15.734    0.000 3404.620    0.005 optimizer.py:84(wrapper)
                 756119    8.438    0.000 3345.951    0.004 grad_mode.py:24(decorate_context)
                 756119   45.757    0.000 3321.673    0.004 adam.py:55(step)
                 756119  255.673    0.000 3226.794    0.004 _functional.py:53(adam)
               48391616  483.594    0.000 3160.554    0.000 distribution.py:34(__init__)
              224000250  210.528    0.000 2910.361    0.000 activation.py:713(forward)
               24195808  237.883    0.000 2730.411    0.000 categorical.py:115(log_prob)
              224000250  218.989    0.000 2699.832    0.000 functional.py:1364(leaky_relu)
              224000250 2437.259    0.000 2437.259    0.000 {built-in method torch._C._nn.leaky_relu}
               73126620  165.538    0.000 2328.402    0.000 optionCritic.py:77(get_Q)
               24195808  307.174    0.000 2282.438    0.000 categorical.py:49(__init__)
                 189029   29.667    0.000 2262.285    0.012 optionCritic.py:116(critic_loss_fn)
               24195808  170.523    0.000 2157.502    0.000 bernoulli.py:34(__init__)
               48580645  166.522    0.000 1818.558    0.000 optionCritic.py:88(get_terminations)
                 756119    3.567    0.000 1543.255    0.002 game.py:42(step)
                 756119    6.876    0.000 1497.194    0.002 layers.py:827(step)
               24195808  933.079    0.000 1389.126    0.000 constraints.py:398(check)
               24195808  193.010    0.000 1099.155    0.000 distribution.py:240(_validate_sample)
                 756119   32.110    0.000  921.881    0.001 layers.py:17(step)
               24195808   59.074    0.000  885.864    0.000 layer.py:106(move)
               74666750   90.802    0.000  847.114    0.000 activation.py:101(forward)
               24195808  828.885    0.000  828.885    0.000 constraints.py:364(check)
               24195808  161.056    0.000  810.894    0.000 bernoulli.py:86(sample)
               24195808  396.128    0.000  759.262    0.000 categorical.py:123(entropy)
               74666750   84.787    0.000  756.312    0.000 functional.py:1195(relu)
             1158199938  754.220    0.000  754.274    0.000 module.py:934(__getattr__)
               24195808  709.647    0.000  709.647    0.000 constraints.py:249(check)
              169370656  695.231    0.000  695.231    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               21171320  686.029    0.000  686.029    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               72587424   94.214    0.000  682.040    0.000 utils.py:106(__get__)
               74666750  658.986    0.000  658.986    0.000 {built-in method relu}
               74666750   67.741    0.000  658.443    0.000 flatten.py:39(forward)
               72965482   79.518    0.000  646.424    0.000 tensor.py:525(__rsub__)
               74666750  590.703    0.000  590.703    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               48391616  206.893    0.000  586.042    0.000 functional.py:46(broadcast_tensors)
               10585660  579.630    0.000  579.630    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 756120   64.263    0.000  565.225    0.001 layers.py:793(update)
               24195808  114.754    0.000  558.508    0.000 layers.py:844(check)
               72965482  555.316    0.000  555.316    0.000 {built-in method rsub}
               10585660  551.508    0.000  551.508    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               24195808  149.606    0.000  536.481    0.000 categorical.py:108(sample)
              900887882  531.944    0.000  531.944    0.000 {built-in method torch._C._get_tracing_state}
               24195808   27.206    0.000  515.452    0.000 categorical.py:88(logits)
               72776453  510.173    0.000  510.173    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               48580645  508.138    0.000  508.138    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                8317309   18.253    0.000  492.959    0.000 tensor.py:575(__iter__)
               24195808   30.571    0.000  488.246    0.000 utils.py:82(probs_to_logits)
               24195808   99.053    0.000  482.012    0.000 utils.py:11(broadcast_all)
             3881304160  473.046    0.000  477.990    0.000 {built-in method builtins.len}
               72587424  472.803    0.000  472.803    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                8317309  463.374    0.000  463.374    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             3644949042  403.272    0.000  403.272    0.000 {method 'values' of 'collections.OrderedDict' objects}
               10585660  402.995    0.000  402.995    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72587424  398.498    0.000  398.498    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               21171320  377.753    0.000  377.753    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10585660  369.280    0.000  369.280    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               24195808  356.833    0.000  356.833    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 189029  284.135    0.002  352.159    0.002 replaybuffer.py:42(sample_option_critic)
               48391616  320.701    0.000  320.701    0.000 {built-in method broadcast_tensors}
               24195808   60.104    0.000  289.044    0.000 utils.py:77(clamp_probs)
                 756119   33.265    0.000  286.266    0.000 replaybuffer.py:34(save_option_critic)
               73154511  258.314    0.000  258.314    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               24195808  248.604    0.000  248.604    0.000 {built-in method bernoulli}
               24195808  235.607    0.000  235.607    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               24195808  228.939    0.000  228.939    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               24356946  221.329    0.000  221.329    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               24195808   50.171    0.000  219.345    0.000 layers.py:838(isFree)
              145552906  218.686    0.000  218.686    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               48391616  198.753    0.000  198.753    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                 756119   34.296    0.000  195.122    0.000 optimizer.py:189(zero_grad)
               24195808  193.895    0.000  193.895    0.000 {built-in method clamp}
                6048960  106.901    0.000  182.061    0.000 layer.py:175(NoRock_update)
              183303822  137.818    0.000  169.173    0.000 layer.py:103(isFree)
               24195808  168.632    0.000  168.632    0.000 {built-in method log}
               24195808  166.783    0.000  166.783    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               72587456   46.659    0.000  155.864    0.000 {built-in method builtins.all}
               72750105  153.861    0.000  153.861    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               24195808  152.843    0.000  152.843    0.000 {built-in method all}
              318444386   99.698    0.000  151.335    0.000 {built-in method builtins.isinstance}
               74666764  147.288    0.000  147.288    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                5103805  141.582    0.000  141.582    0.000 {built-in method tensor}
               24195808  137.210    0.000  137.210    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624153: <Attempt6_Diamonds3_option_critic_0> in cluster <dcc> Done

Job <Attempt6_Diamonds3_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:26 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:27 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258290.20 sec.
    Max Memory :                                 947 MB
    Average Memory :                             929.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15437.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

